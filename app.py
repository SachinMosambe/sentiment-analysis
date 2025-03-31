
import gradio as gr

# Function for prediction
def predictive_system(text):
    # Replace with your prediction logic
    return "Positive" if "good" in text.lower() else "Negative"

# Title and Description
title = "🎥 Movie Sentiment Analysis Application"
description = '''
<div style="text-align: center;">
    <p>Analyze the sentiment of movie reviews with this simple and interactive application.</p>
    <p>Type in a review and find out if the sentiment is <b>Positive</b> or <b>Negative</b>!</p>
</div>
'''

# Interface Design
with gr.Blocks() as app:
    # Centered title and description
    gr.Markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{title}</h1>")
    gr.Markdown(description)

    with gr.Row(equal_height=True):
        # Input section
        with gr.Column(scale=1, min_width=400):
            input_text = gr.Textbox(
                label="Enter Movie Review",
                lines=4,  # Ensure the size matches
                placeholder="Type your movie review here..."
            )

        # Output section
        with gr.Column(scale=1, min_width=400):
            output_text = gr.Textbox(
                label="Sentiment Analysis Result",
                lines=4,  # Same size as input box
                interactive=False
            )

    # Analyze button centered below
    with gr.Row():
        analyze_button = gr.Button("Analyze Sentiment")

    # Footer
    gr.Markdown(
        '''
        <footer style="text-align: center; margin-top: 20px; font-size: small;">
            Created by <b>Sachin Mosambe</b> | Powered by <b>Gradio</b>
        </footer>
        '''
    )

    # Button click functionality
    analyze_button.click(predictive_system, inputs=input_text, outputs=output_text)

# Launch the App
app.launch(share=True)
