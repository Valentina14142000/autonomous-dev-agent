from app.agents.coder import coder_node
from app.agents.executor import executor_node
from app.agents.supervisor import supervisor_node
from app.state import AgentState
from langgraph.graph import END, StateGraph


def evaluation_node(state: AgentState):
  print("---EVALUATOR: ANALYZING EXECUTION RESULTS---")
  iterations = state.get("iteration_count", 0) + 1
  return {"iteration_count": iterations}


def decide_next_step(state: AgentState):
  if state["test_passed"] or state["iteration_count"] >= 2:
    return "end"
  return "retry"


# Construct LangGraph Workflow
workflow = StateGraph(AgentState)

workflow.add_node("supervisor", supervisor_node)
workflow.add_node("coder", coder_node)
workflow.add_node("executor", executor_node)
workflow.add_node("evaluator", evaluation_node)

workflow.set_entry_point("supervisor")
workflow.add_edge("supervisor", "coder")
workflow.add_edge("coder", "executor")
workflow.add_edge("executor", "evaluator")

workflow.add_conditional_edges(
    "evaluator", decide_next_step, {"retry": "coder", "end": END}
)

app_graph = workflow.compile()