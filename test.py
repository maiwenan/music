from snownlp import SnowNLP

s = SnowNLP('欢快的节奏驱散了心中的阴霾，果然音乐赛高~~~~')

print(s.words)
print(s.tags)
print(s.sentiments)
