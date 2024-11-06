# pip install groq-gradio
# pip install --upgrade gradio

import gradio as gr
import groq_gradio
import os

os.environ["GROQ_API_KEY"] = "YOUR GROQ API_KEY"
gr.load(
    name = "llama-3.2-3b-preview",
    src = groq_gradio.registry,
    title = "Groq-Gradio Chat",
    theme =  "upsatwal/mlsc_tiet",
    examples = ["Tell me a short story about a puppy",
                "Write a 14 line poem about travelling in Shakespeare style",
                "What are the wonders of the world?",
                "List the countries in Africa and their capitals"]
).launch()
