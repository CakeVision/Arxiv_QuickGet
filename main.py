import urllib, urllib.request
import arxiv
#url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
#data = urllib.request.urlopen(url)
#print(data.read().decode('utf-8'))
client = arxiv.Client()
search = arxiv.Search(
    query = "abs:ai OR abs:summary OR abs:LLM",
    max_results = 1,
    sort_by = arxiv.SortCriterion.SubmittedDate,
    sort_order = arxiv.SortOrder.Descending
)

results = client.results(search)
def better_split(user_string, word_count):
    output = []
    words = user_string.split(" ")
    for lineNr in range(0,len(words)// word_count +1):
        line = []
        line_len = 0
        while(line_len < word_count and len(words)>0):
            line.append(words[0])
            words.pop(0)
            line_len += 1
        line = " ".join(line)
        print(line)
        output.append(line)

    return output

def split_input(user_string, chunk_size):
    output = []
    words = user_string.split(" ")
    total_length = 0

    while (total_length < len(user_string) and len(words) > 0):
        line = []
        next_word = words[0]
        line_len = len(next_word) + 1

        while  (line_len < chunk_size) and len(words) > 0:
            words.pop(0)
            line.append(next_word)

            if (len(words) > 0):
                next_word = words[0]
                line_len += len(next_word) + 1

        line = " ".join(line)
        output.append(line)
        total_length += len(line) 

    return output
for r in results:
    print(f"ID:{r.entry_id}")
    summary = better_split(r.summary, 6)
    for line in summary:
        print(line)
#for r in results:
    #title_split = split_input(r.title, 40)
    #print("==================================================")
    #print("Title: ")
    #for line in title_split:
    #    print(f"{line}")
    #print(f"\nID:{r.entry_id} \n")
    #print(f"Summary: ")
    #summary_split = better_split(r.summary, 6)
    #for line in summary_split:
    #    print(line)
    #print(f"\n")
    #print("==================================================")
