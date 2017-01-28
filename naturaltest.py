from __future__ import print_function
import semantria
from uuid import uuid4
import time


serializer = semantria.JsonSerializer()

session = semantria.Session("9be4f54f-8900-4ebd-bd76-4812a5f5d820", "6f5ada12-b6e7-4344-900d-8dcce0557bfc", serializer, use_compression=True)

initialTexts = ["Hello world!"]

for text in initialTexts:
	doc = {"id ": str(uuid4()).replace("-", ""), "text": text}

status = session.queueDocument(doc)
if status == 202:
	print("\"", doc["id"], "\" document queued successfully.", "\r\n")

length = len(initialTexts)
results = []

while len(results) < length:
   print("Retrieving your processed results...", "\r\n")
   time.sleep(2)
   # get processed documents
   status = session.getProcessedDocuments()
   results.extend(status)


for data in results:
   # print document sentiment score
   print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")

   # print document themes
   if "themes" in data:
      print("Document themes:", "\r\n")
      for theme in data["themes"]:
         print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")

   # print document entities
   if "entities" in data:
      print("Entities:", "\r\n")
      for entity in data["entities"]:
         print("\t", entity["title"], " : ", entity["entity_type"]," (sentiment: ", entity["sentiment_score"], ")", "\r\n")