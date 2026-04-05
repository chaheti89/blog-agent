def should_continue(state):
    if state.get("outline"):
        return "worker"
    return "end"