from crewai import Crew, Process
from agents import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task

def generate_report(topic):
    # Set up the Crew instance with agents and tasks
    crew = Crew(
        agents=[researcher, writer, proof_reader],
        tasks=[research_task, write_task, proof_read_task],
        process=Process.sequential  # Execute tasks sequentially
    )
    
    # Kick off the process with the given topic and capture result
    result = crew.kickoff(inputs={"topic": topic})
    
    # Try accessing interactions from the result (depends on crewai implementation)
    history = result.get("history", []) if isinstance(result, dict) else []

    # Save agent communication and result in a markdown file
    with open("research.md", "w", encoding="utf-8") as f:
        f.write("# Research Report\n\n")
        
        # Write the agent communication history
        f.write("## Agent Communication\n\n")
        for log in history:
            agent_name = log.get('agent', 'Unknown')
            message = log.get('message', 'No message')
            f.write(f"### {agent_name}\n\n{message}\n\n")

        # Write the final report
        f.write("## Final Report\n\n")
        f.write(result.get("final_report", "No final report available.") if isinstance(result, dict) else str(result))
    
    return "Research report saved in research.md"

# Example usage
topic = "IPL 2025"
output_message = generate_report(topic)
print(output_message)
