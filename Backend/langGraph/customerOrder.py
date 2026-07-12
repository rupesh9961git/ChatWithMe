from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import HumanMessage, AIMessage


def customer(state: MessagesState):
    print(f"[customer] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Customer registered: Rupesh"))
    return state

def search_shop(state: MessagesState):
    print(f"[search_shop] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Shop found: KFC"))
    return state

def place_order(state: MessagesState):
    print(f"[place_order] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Order placed: Chicken Burger"))
    return state

def confirm_order(state: MessagesState):
    print(f"[confirm_order] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Order confirmed"))
    return state

def payment(state: MessagesState):
    print(f"[payment] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Payment successful"))
    return state

def delivery_pickup(state: MessagesState):
    print(f"[delivery_pickup] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Delivery partner assigned: Dunzo"))
    return state

def delivery(state: MessagesState):
    print(f"[delivery] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Order delivered"))
    return state

def feedback(state: MessagesState):
    print(f"[feedback] {state['messages'][-1].content}")
    state["messages"].append(AIMessage(content="Feedback: Great service!"))
    return state


graph = StateGraph(MessagesState)

graph.add_node("customer", customer)
graph.add_node("search_shop", search_shop)
graph.add_node("place_order", place_order)
graph.add_node("confirm_order", confirm_order)
graph.add_node("payment", payment)
graph.add_node("delivery_pickup", delivery_pickup)
graph.add_node("delivery", delivery)
graph.add_node("feedback", feedback)

graph.add_edge(START, "customer")
graph.add_edge("customer", "search_shop")
graph.add_edge("search_shop", "place_order")
graph.add_edge("place_order", "confirm_order")
graph.add_edge("confirm_order", "payment")
graph.add_edge("payment", "delivery_pickup")
graph.add_edge("delivery_pickup", "delivery")
graph.add_edge("delivery", "feedback")
graph.add_edge("feedback", END)

graph = graph.compile()

png = graph.get_graph().draw_mermaid_png()
with open("customer_order_graph.png", "wb") as f:
    f.write(png)

result = graph.invoke({"messages": [HumanMessage(content="I want to order food")]})

for m in result["messages"]:
    print(m.content)
