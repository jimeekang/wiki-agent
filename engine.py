import os
import json
import uuid
from datetime import datetime
import subprocess

class PReinforceEngine:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.meta_dir = os.path.join(root_dir, "20_Meta")
        self.wiki_dir = os.path.join(root_dir, "10_Wiki")
        self.raw_dir = os.path.join(root_dir, "00_Raw")
        
        self.policy_path = os.path.join(self.meta_dir, "Policy.md")
        self.graph_path = os.path.join(self.meta_dir, "Graph.json")
        self.index_path = os.path.join(self.meta_dir, "Index.md")

    def load_graph(self):
        with open(self.graph_path, 'r') as f:
            return json.load(f)

    def save_graph(self, graph):
        with open(self.graph_path, 'w') as f:
            json.dump(graph, f, indent=2)

    def log_policy(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.policy_path, 'a') as f:
            f.write(f"- [{timestamp}] {message}\n")

    def add_to_index(self, title, path):
        link = f"- [[{path}|{title}]]"
        with open(self.index_path, 'r') as f:
            content = f.read()
        
        if link not in content:
            # Simple insertion after navigation section
            parts = content.split("## 📂 Navigation")
            new_content = parts[0] + "## 📂 Navigation\n" + link + "\n" + parts[1]
            with open(self.index_path, 'w') as f:
                f.write(new_content)

    def reinforce_sync(self, action_summary):
        try:
            subprocess.run(["git", "add", "."], cwd=self.root_dir, check=True)
            subprocess.run(["git", "commit", "-m", f"[P-Reinforce] {action_summary}"], cwd=self.root_dir, check=True)
            # subprocess.run(["git", "push", "origin", "main"], cwd=self.root_dir) # Disabled for local safety
            return True
        except Exception as e:
            print(f"Git sync failed: {e}")
            return False

    def process_raw(self, raw_file_path):
        """
        In a real scenario, this would call an LLM to categorize.
        For now, this provides the structure for the agent to use.
        """
        print(f"Processing {raw_file_path}...")
        # (This is where the agent logic would decide the folder and content)
        pass

if __name__ == "__main__":
    engine = PReinforceEngine(".")
    print("P-Reinforce Engine Loaded.")
