import streamlit as st
import openai

# openai.api_key = ""
st.title("TEST")

with st.form("testForm"):
    st.write("Hello World!")
    userinput = st.text_input("prompt")
    submit = st.form_submit_button("submit")
if submit:
    gpt_prompt = []
    gpt_prompt.append(
        {
            "role": "system",
            "content": "Imagine the detail appearance of the input. Response shortly.",
        }
    )

    gpt_prompt.append(
        {
            "role": "user",
            "content": userinput,
        }
    )
    with st.spinner("Wating for DALL-E..."):
        prompt = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=gpt_prompt
        )
        prompt = prompt["choices"][0]["message"]["content"]
        st.caption(prompt)
    with st.spinner("Wating for DALL-E..."):
        result = openai.Image.create(prompt=prompt, size="1024x1024")
        st.image(result["data"][0]["url"])


# import streamlit as st
# import openai

# openai.api_key = ""

# st.title("ChatGPT Plus DALL-E")

# with st.form("form"):
#     user_input = st.text_input("Prompt")
#     submit = st.form_submit_button("Submit")

# if submit:
#     st.write(user_input)

#     # ChatGPT
#     gpt_prompt = []

#     gpt_prompt.append(
#         {
#             "role": "system",
#             "content": "Imagine the detail appearance of the input. Response shortly.",
#         }
#     )

#     gpt_prompt.append({"role": "user", "content": user_input})

#     with st.spinner("Wating for ChatGPT..."):
#         prompt = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo", messages=gpt_prompt
#         )

#     prompt = prompt["choices"][0]["message"]["content"]
#     st.caption(prompt)

#     # DALL-E
#     with st.spinner("Wating for DALL-E..."):
#         result = openai.Image.create(prompt=prompt, size="1024x1024")

#     st.image(result["data"][0]["url"])
