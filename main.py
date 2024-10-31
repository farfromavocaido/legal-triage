import chainlit as cl

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Choose eval framework",
            message="Choose an evaluation framework for the project.",
            icon="/public/admin.png",
            ),

        cl.Starter(
            label="Enquire about this tool",
            message="I would like to learn more about this tool.",
            icon="/public/banner.png",
            )
    ]

@cl.step(type="tool")
async def retrieving_evals():
    # Simulate a "thinking" task with a delay
    await cl.Message (content="🤔 Thinking...").send()
    await cl.sleep(2)  # Adjust the delay here as needed (e.g., 2-4 seconds)
    return("Completed review of evaluation process.")

@cl.step(type="tool")
async def processing_evals():
    await cl.Message(content="🔧 Processing...").send()
    await cl.sleep(4)  # Adjust the delay here as needed (e.g., 2-4 seconds)
    return("Completed processing evaluations.")

@cl.on_message
async def on_message(message: cl.Message):
    # Call the thinking step first
    thinking_message = await retrieving_evals()
    await cl.Message(content=thinking_message).send()

    processing_message = await processing_evals()
    # Send the "thinking" message to the user
    await cl.Message(content=processing_message).send()

    # After the delay, send the image message
    await cl.sleep(1)

    IMAGE_PATH = "public/bossbaby.jpeg"  # Ensure this path is correct and accessible
    await cl.Message(
        content=f"Evaluation of evaluations successful. Result is below:",
        elements=[cl.Image(path=IMAGE_PATH)]  # Using 'path' to load image
    ).send()