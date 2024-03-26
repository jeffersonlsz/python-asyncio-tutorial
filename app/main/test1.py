import requests
from bs4 import BeautifulSoup

url = "https://fatalmodel.com/acompanhantes-imperatriz-ma"

payload = {}
headers = {
  'authority': 'fatalmodel.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': '_ce.irv=new; cebs=1; _ce.clock_event=1; jsCookieTerm18=true; _ce.clock_data=4108%2C45.224.199.176%2C1%2C36489d387fc8bef5e6ceaf2293b7a987; __trf.src=encoded_eyJmaXJzdF9zZXNzaW9uIjp7InZhbHVlIjoiKG5vbmUpIiwiZXh0cmFfcGFyYW1zIjp7fX0sImN1cnJlbnRfc2Vzc2lvbiI6eyJ2YWx1ZSI6Iihub25lKSIsImV4dHJhX3BhcmFtcyI6e319LCJjcmVhdGVkX2F0IjoxNzExMDI4NzQxNjMzfQ==; _gid=GA1.2.398204582.1711028742; rdtrk=%7B%22id%22%3A%228838471b-49a5-470c-bbfb-5a7d64b6b1c0%22%7D; _ga=GA1.1.2091954953.1711027588; __cflb=0H28vgyx35NNX8FcqgmsmWsXQssub2fWeHiTryVWFem; slug-city=imperatriz; XSRF-TOKEN=eyJpdiI6InF0RmJOanNGRzhhWkUxdjFaTWVKdGc9PSIsInZhbHVlIjoiRitNNXNOSU5aby9QQjNtdGxIZHFCa2ZYR1dFKzJXMXBsMzdLbTdQdEJVL3doRHEyTkVwajFRNmE2UWZpenIrTmJHeVNOd2w0VjRDTmJrQWdpZnNlb3c9PSIsIm1hYyI6IjI2YjQ2N2Y2YmY5NjU5YWUyMjhhMjRhYTQzZjQ5OGI2ZjNhMTcyOTBlODQzYzA2Y2Y1YzQ0MDA1ZTFhM2VjOGIiLCJ0YWciOiIifQ%3D%3D; fm_laravel_session=eyJpdiI6ImhJSGlGbVg3WThCR2FzWGxXNTBlcHc9PSIsInZhbHVlIjoiYVRrbEJZdDI4WUYwM0Y4VGRqZElwWXQvU3ZBb0ovMjg5dVlzbFdSQUlKZFBHVGFEUmdBa3BOeU5OT0lUYTlJR0RUWmR5czk3b2ZoYXdVVUlaYXJtVVE9PSIsIm1hYyI6ImU2NjE0MTU2NjViOWNjYjI5MjNhZWYxMDFkYjRlZmQxY2M0ZmIzZWFhMTJhY2FmZWNiMGQzNTNlZWI1MTdjMTgiLCJ0YWciOiIifQ%3D%3D; user_configs_v2=eyJpdiI6IjFUeG1XQVJra2wyTm1jYjRGRWNOZ3c9PSIsInZhbHVlIjoibGVJOUxnNzY4WEpNYm9DcWtIaGQ5THdET0E3OENPUWpoWGhnSkxEc01XZXNQcXdOKzVCTnFjRUZrMHRFZ2RwR2VESUF6Ly9BU3VycVUvcDVPUEhQNlFjZy9weUFLL0dyOWwxUmpVTXFPU0pzWE1BeENjV2Z2VEp6cUJ6cWVLQzRhZkw5bTJVRGpBVnVESGp0alkyT1ZiSkdTWllONktNR2lVUkZKRUVnTWl6ZkpFVmxTRlZMTzloM3p3ZVIzeVkvSml4aGZ0d0k3em1IQkR5WHE3SlZRZmRoQ0NqZnp6SS9tdUEwRmxodVpibVRlZkZ1V0Y4MngrZE1PT0c4K3RuS1lJWFJoM3FMU0RpYmEra0JUd1poODJmUGtzNm95ZjVqRXRzUlVNWVp1Mmc9IiwibWFjIjoiNTVkN2ZhYjA5ODhlZDU5OTViYmZlZGE5MTdlN2Y0MzcwNGJhMTJiZjM1YzJjNzhlN2Y3MGVjOTA5MmUyZDk4YiIsInRhZyI6IiJ9; _ga_80KGM2NV62=GS1.1.1711110228.3.1.1711112866.0.0.0; cebsp_=67; _ce.s=v~417959571a3e17d7187e852ae1d7c4362597f71b~lcw~1711113016602~lva~1711027587774~vpv~0~as~false~v11.fhb~1711073061617~v11.lhb~1711073482508~gtrk.la~lu2oidjv~v11.cs~408548~v11.s~09d0e070-e847-11ee-9a49-a1c568b91ebb~v11.sla~1711113016602~v11.send~1711112866871~lcw~1711113016603; selected_city=eyJpdiI6InRxQ2R1SWRpQlR6R21Td3BFdlJia1E9PSIsInZhbHVlIjoiTnJQaGlmdUxudWNnTmZuUGIzQlZTQT09IiwibWFjIjoiNGQyM2JhMWM0MTE2OGVkN2UzMTU3ZjE5N2Q1YmJhNWZlNmIxN2VkOWFiMzE4NDBhZGM1YzAwNzJiZGQxYmY1YyIsInRhZyI6IiJ9; selected_state=eyJpdiI6IlcyaEZ6ZkhYMVd6M2g0M2hTSUZibUE9PSIsInZhbHVlIjoiQUlKczE5YURBdDgrVEpjb01hRk9SQT09IiwibWFjIjoiMTQ2ZGJjZDJkNmY3Njk0YzM2YzJjODYxOGQ4YjkwYjRlN2IyM2E0YzUxMTM2MjYxYjQzNjk5ZDRhY2JlYzEyMCIsInRhZyI6IiJ9; selected_state_letter=eyJpdiI6IlhUN05pUzZyampRd2l3SFhiQkV1a1E9PSIsInZhbHVlIjoiN05YTEJHazhVYUs2UDJBUlNQZVlEUT09IiwibWFjIjoiODVkMDhiODBhMWFiMjg0ZWQxZWUxNzMyZDI1NmQ1NDkzMDIyYmQxMDBhNzUxYTc0OGU4NGI0MDFmMzhhMDk1OCIsInRhZyI6IiJ9',
  'if-modified-since': 'Fri, 22 Mar 2024 13:04:40 GMT',
  'referer': 'https://fatalmodel.com/acompanhantes-ma',
  'sec-ch-ua': '"Not A(Brand";v="99", "Opera";v="107", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)
site = BeautifulSoup(response.text, "html.parser")

classmodel = "no-tap-highlight rounded-xl relative flex bg-white mx-auto shadow-listing-cards overflow-hidden box-border h-fit w-full"
for elemento in site.find_all('div', class_=classmodel):
    #print(elemento)
    trecho = BeautifulSoup(str(elemento), "html.parser")
    tag_a = trecho.find('a')
    print(tag_a.get('href'))
    
