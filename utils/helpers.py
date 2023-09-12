

def _invoke_agent(agent, question):
    for _ in agent.iter(question):
        _continue = input("Should the agent continue (Y/n)?:\n")
        if _continue != "Y":
            break
