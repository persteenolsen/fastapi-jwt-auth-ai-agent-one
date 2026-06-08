import logging
import traceback
import urllib.parse
from typing import Dict, Any
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

session = requests.Session()

retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)


# ✅ FIXED USER AGENT (demo-friendly, no email)
session.headers.update({
    "User-Agent": "FastAPI-Wikipedia-Demo/1.0",
    "Accept": "application/json",
})

def wikipedia_tool(query: str) -> Dict[str, Any]:
    try:
        # SEARCH
        r = session.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "format": "json"
            },
            timeout=10
        )
        r.raise_for_status()

        results = r.json().get("query", {}).get("search", [])
        if not results:
            return {"success": False, "content": "No results found"}

        title = results[0]["title"]
        safe_title = urllib.parse.quote(title.replace(" ", "_"))

        # SUMMARY
        summary = session.get(
            f"https://en.wikipedia.org/api/rest_v1/page/summary/{safe_title}",
            timeout=10
        )
        summary.raise_for_status()

        data = summary.json()
        extract = data.get("extract", "")

        if not extract or len(extract) < 20:
            return {"success": False, "content": "Empty extract"}

        return {
            "success": True,
            "source": "wikipedia",
            "title": title,
            "content": extract
        }

    except requests.exceptions.RequestException as e:
        logger.warning(f"Wikipedia request failed: {e}")
        return {"success": False, "content": str(e)}

    except Exception as e:
        logger.error(traceback.format_exc())
        return {"success": False, "content": str(e)}