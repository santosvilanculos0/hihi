from datetime import timedelta
from json import loads

from srt import Subtitle, compose


def subtitling0(results: list, srt: str) -> list[Subtitle]:
    WORDS_PER_LINE = 7
    subs: list[Subtitle] = []

    for i, res in enumerate(results):
        jres = loads(res)

        if not "result" in jres:
            continue

        words = jres["result"]

        for j in range(0, len(words), WORDS_PER_LINE):
            line = words[j : j + WORDS_PER_LINE]

            s = Subtitle(
                index=len(subs),
                content=" ".join([l["word"] for l in line]),
                start=timedelta(seconds=line[0]["start"]),
                end=timedelta(seconds=line[-1]["end"]),
            )

            print(s.content)
            subs.append(s)

    return subs


def subtitling(subs: list[Subtitle], srt):
    with open(srt, "w", encoding="UTF-8") as file:
        file.write(compose(subs))
