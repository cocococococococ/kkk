import concurrent
import itertools
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Optional

import requests
import scrapetube
import streamlit as st
# from steamship import PackageInstance


def add_resource(invocation_url: str, api_key: str, url: str):

    # 模拟函数，因为没有steamship
    print(f"Would add resource: {url}")
    return "Simulated response"


def index_youtube_channel(
    channel_url: str, offset: Optional[int] = 0, count: Optional[int] = 10
):
    # instance: PackageInstance = st.session_state.instance
    # 模拟函数，因为没有steamship
    st.warning("YouTube indexing feature requires steamship installation")


def index_youtube_video(youtube_url: str):
    # instance: PackageInstance = st.session_state.instance
    # 模拟函数，因为没有steamship
    st.warning("YouTube video indexing feature requires steamship installation")


COMPANION_DIR = (
    Path(__file__) / ".." / ".." / ".." / "src" / "personalities"
).resolve()


def get_companions():
    return [
        companion.stem
        for companion in COMPANION_DIR.iterdir()
        if companion.suffix == ".json"
    ]


def get_companion_attributes(companion_name: str):
    companion = json.load((COMPANION_DIR / f"{companion_name}.json").open())
    return {
        "name": companion["name"],
        "byline": companion["byline"],
        "identity": "\n".join(companion["identity"]),
        "behavior": "\n".join(companion["behavior"]),
        "profile_image": companion.get("profile_image", ""),
    }
