# TODO#1: Import necessary libraries

# TODO#2: Setup ChromaDB


# TODO#3: Load CLIP model and processor for generating image and text embeddings


# TODO#4: Load and preprocess images

# Measure image ingestion time
start_ingestion_time = time.time()

with torch.no_grad():
    image_embeddings = model.get_image_features(**inputs).numpy()

# Convert numpy arrays to lists
image_embeddings = [embedding.tolist() for embedding in image_embeddings]

# Measure total ingestion time
end_ingestion_time = time.time()
ingestion_time = end_ingestion_time - start_ingestion_time

# TODO#5: Add image embeddings to the collection with metadata and display ingestion time


# TODO#6: Create a function to calculate "accuracy" score based on cosine similarity

# Define Gradio function
def search_image(query):
    # Simple validation: if the query is empty, show an error message
    if not query.strip():
        return None, "Oops! You forgot to type something on the query input!", ""

    print(f"\nQuery: {query}")
    
    # Start measuring the query processing time
    start_time = time.time()
    
    # TODO#7: Generate an embedding for the query text

    # TODO#8: Convert the query embedding from numpy array to a list

    # TODO#9: Perform a vector search in the collection

    # TODO#10: Retrieve the matched image
    
    # Calculate accuracy score based on cosine similarity
    accuracy_score = calculate_accuracy(matched_image_embedding, query_embedding[0])
    
    # End time for query processing
    end_time = time.time()
    query_time = end_time - start_time
    
    # TODO#11: Display result with accuracy, query time, and file name

# Suggested queries
queries = [
    "A group of polar bears",
    "A famous landmark in Paris",
    "A hot pizza fresh from the oven",
    "Food",
    "A Place",
    "A Structure in Europe",
    "Animals"
]

# Function to populate the query input box with the suggested query
def populate_query(suggested_query):
    return suggested_query

# Gradio Interface Layout
with gr.Blocks() as gr_interface:
    gr.Markdown("# Text-to-Image Vector Search using ChromaDB")
    with gr.Row():
        # Left Panel
        with gr.Column():
            # TODO#12: Display the ingestion time of image embeddings
            
            gr.Markdown("### Input Panel")
            
            # Input box for custom query
            custom_query = gr.Textbox(placeholder="Enter your custom query here", label="What are you looking for?")

            # Buttons for cancel and submit actions
            with gr.Row():
                submit_button = gr.Button("Submit Query")
                cancel_button = gr.Button("Cancel")

            # Suggested search phrases as buttons styled like tags
            gr.Markdown("#### Suggested Search Phrases")
            with gr.Row(elem_id="button-container"):
                for query in queries:
                    # Populate the custom_query textbox with the clicked suggested query
                    gr.Button(query).click(fn=lambda q=query: q, outputs=custom_query)

        # Right Panel
        with gr.Column():
            gr.Markdown("### Retrieved Image")
            # TODO#13: Output for image result
            
            # Output for accuracy score and query time
            accuracy_output = gr.Textbox(label="Performance")

        # Button click handler for custom query submission
        submit_button.click(fn=search_image, inputs=custom_query, outputs=[image_output, accuracy_output])

        # Cancel button to clear the inputs
        cancel_button.click(fn=lambda: (None, ""), outputs=[image_output, accuracy_output])

# TODO#14: Launch the Gradio interface
