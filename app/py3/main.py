"""A simple HTTP server to show problems and tags.
   TODO: Do navigation from tags and from problems to code or tags.

"""
import glob
import os
from collections import defaultdict
from pathlib import Path
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

def get_file_as_str(f):
    return Path(f).read_text()
def linkify(anchor_text, anchor_ref):
    return "<a href={}>{}</a>".format(anchor_ref, anchor_text)
def linkify_tag(tag):
    return linkify(tag, "/tag/"+tag)
def linkify_prob(prob):
    return linkify(prob, "https://leetcode.com/problems/" + prob)

users = set()
all_tags = set()
tags_dict = defaultdict(set)
sol_dict = defaultdict(set)
prob_tags_dict = defaultdict(set)
probs = os.listdir('../../problems')

def load_info():
    global users
    global all_tags
    global tags_dict
    global sol_dict
    global prob_tags_dict
    global probs
    users = set()
    all_tags = set()
    tags_dict = defaultdict(set)
    sol_dict = defaultdict(set)
    prob_tags_dict = defaultdict(set)
    
    probs = os.listdir('../../problems')
    # location of TAG files
    tag_files = glob.glob('../../problems/*/*/TAGS')
    for tag_file in tag_files:
        with open(tag_file, 'r') as f:
            lines = f.readlines()
            prob = tag_file.rpartition("../../problems/")[2].split("/")[0]
            users.add(tag_file.rpartition("../../problems/")[2].split("/")[1])
            for line in lines:
                tags = line.split(',')
                sol_file = tags[0]
                sol_file_path = tag_file.replace('TAGS', sol_file)
                sol_dict[prob].add(sol_file_path)
                for tg in tags[1:]:
                    tag = tg.strip()
                    all_tags.add(linkify_tag(tag)) 
                    tags_dict[tag].add(sol_file_path)
                    prob_tags_dict[prob].add(tag)


def handler_class(callback):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            load_info()
            if self.path.startswith("/solutions/"):
                prob = self.path[11:]
                print('solutions requeted for ' + prob)
                sols = sol_dict[prob]
                fcontent = ""
                for path in sols:
                    fcontent = fcontent + "<h2>" + path + "</h2><pre>" + get_file_as_str(path) + "</pre>"
                content = fcontent
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content.encode("ascii"))
            if self.path.startswith("/tag/"):
                tag = self.path[5:]
                paths = tags_dict[tag]
                fcontent = ""
                for path in paths:
                    fcontent = fcontent + "<h2>" + path + "</h2><pre>" + get_file_as_str(path) + "</pre>"
                content = fcontent
                
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content.encode("ascii"))
            elif self.path != "/":
                self.send_response(404)
                content = "not found"
                self.send_header("Content-Type", "text/plain")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
                return
            content = callback(probs)
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content.encode("ascii"))
    return Handler

class ProgressServer(HTTPServer):
    def __init__(self, callback, port=8888):
        super().__init__(('', port), handler_class(callback))
    def start_async(self):
        self.thread = Thread(target=self.serve_forever, daemon=False)
        self.thread.start()
    """
    def join(self):
        self.shutdown()
        self.thread.join()
    """

if __name__ == '__main__':
    PORT = 8888
    load_info()
    probs_str = ""
    def tag_links_for_prob(p):
        tags = prob_tags_dict[p]
        return '  (' + ','.join([linkify_tag(tag) for tag in tags]) + ')'
    def sol_links_for_prob(p):
        return linkify(' [solutions] ', '/solutions/'+p)
    def get_probs_str(myprobs):
        return str('<br/> '.join(sorted([linkify_prob(p) + sol_links_for_prob(p) + tag_links_for_prob(p) for p in myprobs])))
    p = ProgressServer(port=PORT, callback=lambda myprobs: "<h1>problems:</h1> " + get_probs_str(myprobs)+ "<h1> tags:</h1>" + str(sorted(all_tags)))
    print("http://localhost:8888/")
    p.start_async()


