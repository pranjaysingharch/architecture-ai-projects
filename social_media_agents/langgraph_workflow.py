# LangGraph-based workflow for social media content research, writing, and publishing
# Install langgraph: pip install langgraph

from langgraph import Workflow, Node, Context

# Agent Nodes
class ResearchAgent(Node):
    def run(self, ctx: Context):
        import requests
        research_tasks = ctx.get('research_tasks', ["Find trending topics"])
        results = []
        for task in research_tasks:
            if task == "Find trending topics":
                results.append(["AI in Marketing", "Remote Work Trends", "Sustainable Business"])
            elif task == "Analyze competitors":
                results.append(["Competitor A: High engagement", "Competitor B: New campaign"])
            elif task == "Web search":
                # Example: Use DuckDuckGo Instant Answer API (no key required)
                query = ctx.get('web_query', 'AI trends')
                response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
                if response.status_code == 200:
                    data = response.json()
                    abstract = data.get('Abstract', 'No summary found.')
                    results.append([f"Web search result for '{query}': {abstract}"])
                else:
                    results.append([f"Web search failed for '{query}'."])
            else:
                results.append([f"Result for {task}"])
        ctx['research_results'] = results
        print("ResearchAgent: Results", results)
        return ctx

class WritingAgent(Node):
    def run(self, ctx: Context):
        import requests
        writing_tasks = ctx.get('writing_tasks', ["Write articles"])
        articles = []
        for task in writing_tasks:
            if task == "Write articles":
                topics = ctx.get('research_results', [[]])[0]
                for topic in topics:
                    articles.append(f"Article about {topic}:\nThis is a sample article discussing {topic}.")
            elif task == "Summarize research":
                summary = "Summary: " + ", ".join(str(r) for r in ctx.get('research_results', []))
                articles.append(summary)
            elif task == "GitHub search":
                # Example: Search GitHub repositories using GitHub API
                response = requests.get("https://api.github.com/search/repositories?q=langgraph")
                if response.status_code == 200:
                    data = response.json()
                    repo_names = [item['full_name'] for item in data.get('items', [])]
                    articles.append(f"GitHub Search Results for 'langgraph':\n" + "\n".join(repo_names))
                else:
                    articles.append("GitHub search failed.")
            else:
                articles.append(f"Result for writing task: {task}")
        ctx['articles'] = articles
        # Write results to MDX file
        with open("output.mdx", "w") as f:
            for article in articles:
                f.write(f"{article}\n\n")
        print("WritingAgent: Articles/Summaries written and GitHub results saved to output.mdx")
        return ctx

class PublishingAgent(Node):
    def run(self, ctx: Context):
        # Handle multiple publishing tasks
        publishing_tasks = ctx.get('publishing_tasks', ["Publish to LinkedIn"])
        for task in publishing_tasks:
            if task == "Publish to LinkedIn":
                for article in ctx.get('articles', []):
                    print("PublishingAgent: Publishing article to LinkedIn...")
                    print(article)
            elif task == "Schedule posts":
                print("PublishingAgent: Scheduling posts...")
            else:
                print(f"PublishingAgent: Handling publishing task: {task}")
        ctx['published'] = True
        return ctx

# Orchestrate workflow
workflow = Workflow()
workflow.add_node('research', ResearchAgent())
workflow.add_node('writing', WritingAgent())
workflow.add_node('publishing', PublishingAgent())
workflow.add_edge('research', 'writing')
workflow.add_edge('writing', 'publishing')

if __name__ == "__main__":
    ctx = Context()
    ctx['research_tasks'] = ["Find trending topics", "Analyze competitors"]
    ctx['writing_tasks'] = ["Write articles", "Summarize research"]
    ctx['publishing_tasks'] = ["Publish to LinkedIn", "Schedule posts"]
    workflow.run('research', ctx)
