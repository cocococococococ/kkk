import streamlit as st


def sidebar():
    with st.sidebar:
        api_key = st.text_input(
            "Steamship API Key (not required in demo mode)",
            value=st.session_state.get(
                "steamship_api_key", ""
            )
                  or "",
            type="password",
        )
        if api_key:
            st.session_state.steamship_api_key = api_key

        st.write(
            "[👀 View the source code](https://github.com/steamship-packages/langchain-production-starter)"
        )
        st.write("[✉️ Send feedback](https:///)")

        # "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

        if instance := st.session_state.get("instance"):
            st.write(
                f"Instance: {instance.get('config', {}).get('name', 'Unknown')}"
            )


def get_api_key():
    # 返回一个模拟的API密钥，因为不需要真正的steamship
    if "steamship_api_key" not in st.session_state:
        st.session_state.steamship_api_key = "demo-key"
    return st.session_state.steamship_api_key


def get_instance():
    instance = st.session_state.get("instance")
    if not instance:
        st.warning('First create your chatbot by clicking "Chatbot"')
        st.stop()
    else:
        return instance


def show_response(response):
    if isinstance(response, str):
        st.write(response)
    else:
        # 处理其他类型的响应
        if "text" in response:
            st.write(response["text"])
        elif "url" in response:
            st.write(f"[Link]({response['url']})")
        else:
            st.write(str(response))
