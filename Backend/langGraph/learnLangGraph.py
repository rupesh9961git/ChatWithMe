from langgraph.graph import StateGraph, START, END

def greet(state):
    print(f"Hello {state['name']}! How can I assist you today?")
    return state

graph = StateGraph(dict)

graph.add_node("greet", greet)

graph.add_edge(START, "greet")
graph.add_edge("greet", END)

graph = graph.compile()
# print(graph.get_graph().draw_mermaid_png())

png = graph.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png)

graph.invoke({
    "name": "Rupesh"
})