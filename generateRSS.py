import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime, timezone

def prettify_xml(element):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def generate_rss(feed_title, feed_link, feed_description, items):
    """Generate an RSS XML file."""
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    # Add channel metadata
    ET.SubElement(channel, "title").text = feed_title
    ET.SubElement(channel, "link").text = feed_link
    ET.SubElement(channel, "description").text = feed_description
    ET.SubElement(channel, "lastBuildDate").text = feed_lastBuildDate

    # Add items to the RSS feed
    for item in items:
        item_element = ET.SubElement(channel, "item")
        ET.SubElement(item_element, "title").text = item["title"]
        ET.SubElement(item_element, "link").text = item["link"]
        ET.SubElement(item_element, "description").text = item["description"]
        ET.SubElement(item_element, "pubDate").text = item["pubDate"]

    # Return the pretty-printed XML string
    return prettify_xml(rss)

# Example usage
if __name__ == "__main__":
    feed_title = "My RSS Feed"
    feed_link = "https://mwood11549.github.io/"
    feed_description = "This is a sample RSS feed."
    feed_lastBuildDate = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    items = [
        {
            "title": "Daily Item",
            "link": "https://mwood11549.github.io/",
            "description": "Daily Updates.",
            "pubDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        },
        {
            "title": "Weekly Item",
            "link": "https://mwood11549.github.io/",
            "description": "Weekly Updates.",
            "pubDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        },
        {
            "title": "Monthly Item",
            "link": "https://mwood11549.github.io/",
            "description": "Monthly Updates.",
            "pubDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        },
        {
            "title": "Yearly Item",
            "link": "https://mwood11549.github.io/",
            "description": "Yearly Updates.",
            "pubDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        }
    ]

    rss_xml = generate_rss(feed_title, feed_link, feed_description, items)

    # Save to a file
    with open("rss_feed.xml", "w", encoding="utf-8") as file:
        file.write(rss_xml)

    print("RSS feed generated and saved as 'rss_feed.xml'.")
