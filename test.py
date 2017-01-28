import semantria, time, uuid

#some sample text
initialTexts = [
    "Lisa - there's 2 Skinny cow coupons available $5 skinny cow ice cream coupons on special k boxes and Printable FPC from facebook - a teeny tiny cup of ice cream. I printed off 2 (1 from my account and 1 from dh's). I couldn't find them instore and i'm not going to walmart before the 19th. Oh well sounds like i'm not missing much ...lol",
    "In Lake Louise - a guided walk for the family with Great Divide Nature Tours  rent a canoe on Lake Louise or Moraine Lake  go for a hike to the Lake Agnes Tea House. In between Lake Louise and Banff - visit Marble Canyon or Johnson Canyon or both for family friendly short walks. In Banff  a picnic at Johnson Lake  rent a boat at Lake Minnewanka  hike up Tunnel Mountain  walk to the Bow Falls and the Fairmont Banff Springs Hotel  visit the Banff Park Museum. The \"must-do\" in Banff is a visit to the Banff Gondola and some time spent on Banff Avenue - think candy shops and ice cream. Have a Fanta while you're there.",
    "On this day in 1786 - In New York City  commercial ice cream was manufactured for the first time."
]
for text in initialTexts:
   doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}

session = semantria.Session("9be4f54f-8900-4ebd-bd76-4812a5f5d820", "6f5ada12-b6e7-4344-900d-8dcce0557bfc")
#queue a batch of documents
session.queueBatch(initialTexts)
#keep track of how many we sent
number_of_docs = len(initialTexts)
results = []
#keep polling for results until we got everything back
while len(results) < number_of_docs:
  time.sleep(3)
  status = session.getProcessedDocuments()
  if isinstance(status, list):
        for object_ in status:
            results.append(object_)
