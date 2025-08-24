# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO: REMOVE THIS CELL FROM YOUR NOTEBOOK ###

import re
from urllib.parse import quote

from IPython.display import Markdown, display


def generate_html(file_path: str):
    match = re.search(
        r"(?:https://)?(?:github\.com/)?(?:GoogleCloudPlatform/)?(?:generative-ai/)?(?:blob/)?(?:main/)?([\w/-]+.ipynb)",
        file_path,
    )
    if not match:
        return "Could not generate table."

    file_path = match.group(1)

    base_url = "https://github.com/GoogleCloudPlatform/generative-ai/blob/main/"
    raw_github_url = (
        "https://raw.githubusercontent.com/GoogleCloudPlatform/generative-ai/main/"
    )

    colab_url = "https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/"
    colab_enterprise_url = f"https://console.cloud.google.com/vertex-ai/colab/import/{raw_github_url.replace('/', '%2F')}"
    vertex_ai_url = f"https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url={raw_github_url}"
    bigquery_studio_url = (
        f"https://console.cloud.google.com/bigquery/import?url={base_url}"
    )

    linkedin_url = "https://www.linkedin.com/sharing/share-offsite/?url="
    bluesky_url = "https://bsky.app/intent/compose?text="
    twitter_url = "https://twitter.com/intent/tweet?url="
    reddit_url = "https://reddit.com/submit?url="
    facebook_url = "https://www.facebook.com/sharer/sharer.php?u="

    encoded_url = quote(f"{base_url}{file_path}")

    html = f"""
```html
<table align="left">
  <td style="text-align: center">
    <a href="{colab_url}{file_path}">
      <img width="32px" src="https://www.gstatic.com/pantheon/images/bigquery/welcome_page/colab-logo.svg" alt="Google Colaboratory logo"><br> Open in Colab
    </a>
  </td>
  <td style="text-align: center">
    <a href="{colab_enterprise_url}{file_path.replace('/', '%2F')}">
      <img width="32px" src="https://lh3.googleusercontent.com/JmcxdQi-qOpctIvWKgPtrzZdJJK-J3sWE1RsfjZNwshCFgE_9fULcNpuXYTilIR2hjwN" alt="Google Cloud Colab Enterprise logo"><br> Open in Colab Enterprise
    </a>
  </td>
  <td style="text-align: center">
    <a href="{vertex_ai_url}{file_path}">
      <img src="https://www.gstatic.com/images/branding/gcpiconscolors/vertexai/v1/32px.svg" alt="Vertex AI logo"><br> Open in Vertex AI Workbench
    </a>
  </td>"""

    # Add BigQuery Studio link only if the flag is True
    if INCLUDE_BIGQUERY_STUDIO:
        html += f"""
  <td style="text-align: center">
    <a href="{bigquery_studio_url}{file_path}">
      <img src="https://www.gstatic.com/images/branding/gcpiconscolors/bigquery/v1/32px.svg" alt="BigQuery Studio logo"><br> Open in BigQuery Studio
    </a>
  </td>"""

    html += f"""
  <td style="text-align: center">
    <a href="{base_url}{file_path}">
      <img width="32px" src="https://www.svgrepo.com/download/217753/github.svg" alt="GitHub logo"><br> View on GitHub
    </a>
  </td>
</table>

<div style="clear: both;"></div>

<b>Share to:</b>

<a href="{linkedin_url}{encoded_url}" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" alt="LinkedIn logo">
</a>

<a href="{bluesky_url}{encoded_url}" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Bluesky_Logo.svg" alt="Bluesky logo">
</a>

<a href="{twitter_url}{encoded_url}" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/5/5a/X_icon_2.svg" alt="X logo">
</a>

<a href="{reddit_url}{encoded_url}" target="_blank">
  <img width="20px" src="https://redditinc.com/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png" alt="Reddit logo">
</a>

<a href="{facebook_url}{encoded_url}" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook logo">
</a>
```"""
    return html


# File path from the repository root
file_path = "notebook_template.ipynb"  # @param {type:"string"}

# Include link to Open in BigQuery Studio
INCLUDE_BIGQUERY_STUDIO = False  # @param {type:"boolean"}
display(Markdown(generate_html(file_path)))


import sys

if "google.colab" in sys.modules:
    from google.colab import auth

    auth.authenticate_user()

# Use the environment variable if the user doesn't provide Project ID.
import os

PROJECT_ID = "[your-project-id]"  # @param {type: "string", placeholder: "[your-project-id]", isTemplate: true}
if not PROJECT_ID or PROJECT_ID == "[your-project-id]":
    PROJECT_ID = str(os.environ.get("GOOGLE_CLOUD_PROJECT"))

LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "global")

from google import genai

client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

from IPython.display import Markdown, display

# TODO: Add all library imports here

MODEL_ID = "gemini-2.0-flash"  # @param {type:"string"}
