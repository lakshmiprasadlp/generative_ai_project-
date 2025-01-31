import streamlit as st
from crewai import Crew, Process
from agents import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task

# Create the Crew instance
crew = Crew(
  agents=[researcher, writer, proof_reader],
  tasks=[research_task, write_task, proof_read_task],
  process=Process.sequential
)

def generate_report(topic):
  # Kickoff the crew process with the given topic
  result = crew.kickoff(inputs={"topic": topic})
  return result
# Streamlit UI
st.title('AI-powered Technology Intelligence & Storytelling')
st.header('Enter a Topic to Generate a Report')
# Take input from the user
topic = st.text_input('Topic', 'Artificial Intelligence in Finance')
if st.button('Generate Report'):
  if topic:
    with st.spinner('Generating Report...'):
      result = generate_report(topic)
      st.success('Report Generated!')
      # Display the result
      st.subheader(f"Generated Report for {topic}:")
      st.markdown(result)
  else:
    st.warning("Please enter a topic to generate the report.")



















