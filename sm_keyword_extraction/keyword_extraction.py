'''
python 2 version
'''

from collections import Counter
import nltk
import operator
from summa import keywords

test = '''
I'm here today to talk to you about a very powerful little word, one that people will do almost anything to avoid becoming. Billion-dollar industries thrive because of the fear of it, and those of us who undeniably are it are left to navigate a relentless storm surrounding it. I'm not sure if any of you have noticed, but I'm fat. Not the lowercase, muttered-behind-my-back kind, or the seemingly harmless chubby or cuddly. I'm not even the more sophisticated voluptuous or curvaceous kind. Let's not sugarcoat it. I am the capital F-A-T kind of fat. I am the elephant in the room. When I walked out on stage, some of you may have been thinking, "Aww, this is going to be hilarious, because everybody knows that fat people are funny." (Laughter) Or you may have been thinking, "Where does she get her confidence from?" Because a confident fat woman is almost unthinkable. The fashion-conscious members of the audience may have been thinking how fabulous I look in this Beth Ditto dress -- (Cheers) thank you very much. Whereas some of you might have thought, "Hmm, black would have been so much more slimming." (Laughter) You may have wondered, consciously or not, if I have diabetes, or a partner, or if I eat carbs after 7pm. (Laughter) You may have worried that you ate carbs after 7pm last night, and that you really should renew your gym membership. These judgments are insidious. They can be directed at individuals and groups, and they can also be directed at ourselves. And this way of thinking is known as fatphobia. Like any form of systematic oppression, fatphobia is deeply rooted in complex structures like capitalism, patriarchy and racism, and that can make it really difficult to see, let alone challenge. We live in a culture where being fat is seen as being a bad person -- lazy, greedy, unhealthy, irresponsible and morally suspect. And we tend to see thinness as being universally good -- responsible, successful, and in control of our appetites, bodies and lives. We see these ideas again and again in the media, in public health policy, doctors' offices, in everyday conversations and in our own attitudes. We may even blame fat people themselves for the discrimination they face because, after all, if we don't like it, we should just lose weight. Easy. This antifat bias has become so integral, so ingrained to how we value ourselves and each other that we rarely question why we have such contempt for people of size and where that disdain comes from. But we must question it, because the enormous value we place on how we look affects every one of us. And do we really want to live in a society where people are denied their basic humanity if they don't subscribe to some arbitrary form of acceptable? So when I was six years old, my sister used to teach ballet to a bunch of little girls in our garage. I was about a foot taller and a foot wider than most of the group. When it came to doing our first performance, I was so excited about wearing a pretty pink tutu. I was going to sparkle. As the other girls slipped easily into their Lycra and tulle creations, not one of the tutus was big enough to fit me. I was determined not to be excluded from the performance, so I turned to my mother and loud enough for everyone to hear said, "Mom, I don't need a tutu. I need a fourfour." (Laughter) Thanks, Mom. (Applause) And although I didn't recognize it at the time, claiming space for myself in that glorious fourfour was the first step towards becoming a radical fat activist. Now, I'm not saying that this whole body-love thing has been an easy skip along a glittering path of self-acceptance since that day in class. Far from it. I soon learned that living outside what the mainstream considers normal can be a frustrating and isolating place. I've spent the last 20 years unpacking and deprogramming these messages, and it's been quite the roller coaster. I've been openly laughed at, abused from passing cars and been told that I'm delusional. I also receive smiles from strangers who recognize what it takes to walk down the street with a spring in your step and your head held high. (Cheer) Thanks. And through it all, that fierce little six-year-old has stayed with me, and she has helped me stand before you today as an unapologetic fat person, a person that simply refuses to subscribe to the dominant narrative about how I should move through the world in this body of mine. (Applause) And I'm not alone. I am part of an international community of people who choose to, rather than passively accepting that our bodies are and probably always will be big, we actively choose to flourish in these bodies as they are today. People who honor our strength and work with, not against, our perceived limitations, people who value health as something much more holistic than a number on an outdated BMI chart. Instead, we value mental health, self-worth and how we feel in our bodies as vital aspects to our overall well-being. People who refuse to believe that living in these fat bodies is a barrier to anything, really. There are doctors, academics and bloggers who have written countless volumes on the many facets of this complex subject. There are fatshionistas who reclaim their bodies and their beauty by wearing fatkinis and crop tops, exposing the flesh that we're all taught to hide. There are fat athletes who run marathons, teach yoga or do kickboxing, all done with a middle finger firmly held up to the status quo. And these people have taught me that radical body politics is the antidote to our body-shaming culture. But to be clear, I'm not saying that people shouldn't change their bodies if that's what they want to do. Reclaiming yourself can be one of the most gorgeous acts of self-love and can look like a million different things, from hairstyles to tattoos to body contouring to hormones to surgery and yes, even weight loss. It's simple: it's your body, and you decide what's best to do with it. My way of engaging in activism is by doing all the things that we fatties aren't supposed to do, and there's a lot of them, inviting other people to join me and then making art about it. The common thread through most of this work has been reclaiming spaces that are often prohibitive to bigger bodies, from the catwalk to club shows, from public swimming pools to prominent dance stages. And reclaiming spaces en masse is not only a powerful artistic statement but a radical community-building approach. This was so true of "AQUAPORKO!" -- (Laughter) the fat fem synchronized swim team I started with a group of friends in Sydney. The impact of seeing a bunch of defiant fat women in flowery swimming caps and bathers throwing their legs in the air without a care should not be underestimated. (Laughter) Throughout my career, I have learned that fat bodies are inherently political, and unapologetic fat bodies can blow people's minds. When director Kate Champion, of acclaimed dance theater company Force Majeure, asked me to be the artistic associate on a work featuring all fat dancers, I literally jumped at the opportunity. And I mean literally. "Nothing to Lose" is a work made in collaboration with performers of size who drew from their lived experiences to create a work as varied and authentic as we all are. And it was as far from ballet as you could imagine. The very idea of a fat dance work by such a prestigious company was, to put it mildly, controversial, because nothing like it had ever been done on mainstream dance stages before anywhere in the world. People were skeptical. "What do you mean, 'fat dancers?' Like, size 10, size 12 kind of fat? Where did they do their dance training? Are they going to have the stamina for a full-length production?" But despite the skepticism, "Nothing to Lose" became a sellout hit of Sydney Festival. We received rave reviews, toured, won awards and were written about in over 27 languages. These incredible images of our cast were seen worldwide. I've lost count of how many times people of all sizes have told me that the show has changed their lives, how it helped them shift their relationship to their own and other people's bodies, and how it made them confront their own bias. But of course, work that pushes people's buttons is not without its detractors. I have been told that I'm glorifying obesity. I have received violent death threats and abuse for daring to make work that centers fat people's bodies and lives and treats us as worthwhile human beings with valuable stories to tell. I've even been called "the ISIS of the obesity epidemic" -- (Laughter) a comment so absurd that it is funny. But it also speaks to the panic, the literal terror, that the fear of fat can evoke. It is this fear that's feeding the diet industry, which is keeping so many of us from making peace with our own bodies, for waiting to be the after-photo before we truly start to live our lives. Because the real elephant in the room here is fatphobia. Fat activism refuses to indulge this fear. By advocating for self-determination and respect for all of us, we can shift society's reluctance to embrace diversity and start to celebrate the myriad ways there are to have a body. Thank you. (Applause)
'''

token = nltk.word_tokenize(test)


# Calculate term frequency
counter = Counter(token).most_common()


# keeping order of words in text, store term frequency
aaa = list(token)
unsortedlist = []
finished = []   # Preventing data redundancy, store a data processed
for a in aaa:
    if not a in finished:
        for c in counter:
            if a == c[0]:
                unsortedlist.append([a, c[1]])
                finished.append(a)

# the unsorted list that keeps order and has term frequency are tagged by part-of-speech
pos = nltk.pos_tag([word[0] for word in unsortedlist])

# original text is converted to tokenized word in list
words = list(token)


# syntactic filtering (Noun and Adjective)
NNlist = []
for tag in pos:
    if tag[1] == 'NN' or tag[1] == 'NNS' or tag[1] == 'NNP' or tag[1] == 'NNPS' or tag[1] == 'JJ' or tag[1] == 'JJR' or tag[1] == 'JJS':
        NNlist.append(tag)


# Integrate [words, term frequency] and pos
candidates = []
for tag in NNlist:
    for word in counter:
        if tag[0] == word[0]:
            tmp = []
            tmp.append(word[0])
            tmp.append(word[1])
            tmp.append(tag[1])
            candidates.append(tmp)

print 'candidates with tf+pos tagging : ', len(candidates), candidates


# A keyword can be consist of multi-words. (2 or 3 words)
# For this reason, candidate keywords have to check the case.
# I considered keywords having two or three words.
print 'Multi Keyword Processing...'
multiKeywords = []
dealtWith = []
i = 0
DoPop = False

while i < len(candidates)-1:
    DoPop = False
    firstWord = candidates[i][0]
    secondWord = candidates[i+1][0]

    if i < len(candidates)-2:
        thirdWord = candidates[i+2][0]
        index = words.index(firstWord)
        multiNum = 1
        IsTwo = True
        j = 0
        pos = ''
        importance = 0

        if words[index+1] == secondWord:
            multiword = firstWord+' '+secondWord

            if words[index+2] == thirdWord :
                multiword = multiword + ' ' + thirdWord
                multiNum = 2
                IsTwo = False

            multicount = test.count(multiword)

            if IsTwo:
                while j < multicount:
                    p = words.index(candidates[i][0])
                    words.pop(p)
                    j += 1
                j = 0
                while j < multicount:
                    p = words.index(candidates[i+1][0])
                    words.pop(p)
                    j += 1
            else:
                while j < multicount:
                    p = words.index(candidates[i][0])
                    words.pop(p)
                    j += 1
                j = 0
                while j < multicount:
                    p = words.index(candidates[i+1][0])
                    words.pop(p)
                    j += 1
                j = 0
                while j < multicount:
                    p = words.index(candidates[i+2][0])
                    words.pop(p)
                    j += 1
            j = 0

            while j <= multiNum :
                pos += candidates[i+j][2] + ' '
                candidates[i+j][1] -= multicount
                if candidates[i+j][1] == 0 :
                    candidates.pop(i+j)
                    DoPop = True
                    j -= 1
                    multiNum -= 1
                j += 1

            multikeyword = [multiword, multicount, pos]
            multiKeywords.append(multikeyword)
        else :
            multiKeywords.append(candidates[i])
    else:
        index = words.index(firstWord)
        j = 0

        if words[index+1] == secondWord:
            multiword = firstWord+' '+secondWord
            multicount = test.count(multiword)

            while j < multicount:
                p = words.index(candidates[i][0])
                words.pop(p)
                j += 1
            while j < multicount:
                p = words.index(candidates[i+1][0])
                words.pop(p)
                j += 1

            pos = candidates[i][2] + ' ' + candidates[i+1][2] + ' '
            candidates[i][1] -= multicount
            candidates[i+1][1] -= multicount

            if candidates[i][1] == 0 and candidates[i+1][1] == 0:
                candidates.pop(i)
                candidates.pop(i)
                DoPop = True
            else:
                if candidates[i][1] == 0:
                    candidates.pop(i)
                    DoPop = True
                elif candidates[i + 1][1] == 0:
                    candidates.pop(i + 1)
                    DoPop = True

            multikeyword = [multiword, multicount, pos]
            multiKeywords.append(multikeyword)
        else :
            multiKeywords.append(candidates[i])

    if not DoPop:
        i += 1

for word in candidates:
    if not word[0] in [x[0] for x in multiKeywords] and word[1] is not 0:
        multiKeywords.append(word)

print 'Multi keywords : ', len(multiKeywords), multiKeywords


# Calculate TextRank for keyword extraction (using MIT's implementation, summa for TextRank)
textrank = keywords.keywords(test, ratio=1.0, scores=True)

# Integrate  [words, term frequency, pos] and importance gotten by TextRank
final_keywords = []
for keyword in multiKeywords:
    for rank in textrank:
        if keyword[0] == rank[0]:
            keyword.append(rank[1])
            final_keywords.append(keyword)

    if len(keyword) == 3:
        keyword.append(0.01)
        final_keywords.append(keyword)

print 'final keywords : ', len(final_keywords), final_keywords

"""
# A keyword can be consist of multi-words. (2 or 3 words)
# For this reason, candidate keywords have to check the case.
# I considered keywords having two or three words.
print 'Multi Keyword Processing...'
modifiedKeywords = []
dealtWith = []
i = 0
DoPop = False

while i < len(final_keywords)-1:
    DoPop = False
    firstWord = final_keywords[i][0]
    secondWord = final_keywords[i+1][0]

    if i < len(final_keywords)-2:
        thirdWord = final_keywords[i+2][0]
        index = words.index(firstWord)
        multiNum = 1
        IsTwo = True
        j = 0
        pos = ''
        importance = 0

        if words[index+1] == secondWord:
            multiword = firstWord+' '+secondWord

            if words[index+2] == thirdWord :
                multiword = multiword + ' ' + thirdWord
                multiNum = 2
                IsTwo = False

            multicount = test.count(multiword)

            if IsTwo:
                while j < multicount:
                    p = words.index(final_keywords[i][0])
                    words.pop(p)
                    j += 1
                j = 0
                while j < multicount:
                    p = words.index(final_keywords[i+1][0])
                    words.pop(p)
                    j += 1
            else:
                while j < multicount:
                    p = words.index(final_keywords[i][0])
                    words.pop(p)
                    j += 1
                j = 0
                while j < multicount:
                    p = words.index(final_keywords[i+1][0])
                    words.pop(p)
                    j += 1
                j = 0
                while j < multicount:
                    p = words.index(final_keywords[i+2][0])
                    words.pop(p)
                    j += 1
            j = 0

            loopNum = 0
            while j <= multiNum :
                pos += final_keywords[i+j][2] + ' '
                importance += final_keywords[i+j][3]
                final_keywords[i+j][1] -= multicount

                if final_keywords[i+j][1] == 0 :
                    final_keywords.pop(i+j)
                    DoPop = True
                    j -= 1
                    multiNum -= 1

                loopNum += 1
                j += 1

            importance /= loopNum
            multikeyword = [multiword, multicount, pos, importance]
            modifiedKeywords.append(multikeyword)
        else :
            modifiedKeywords.append(final_keywords[i])
    else:
        index = words.index(firstWord)
        j = 0

        if words[index+1] == secondWord:
            multiword = firstWord+' '+secondWord
            multicount = test.count(multiword)

            while j < multicount:
                p = words.index(final_keywords[i][0])
                words.pop(p)
                j += 1
            while j < multicount:
                p = words.index(final_keywords[i+1][0])
                words.pop(p)
                j += 1

            pos = final_keywords[i][2] + ' ' + final_keywords[i+1][2] + ' '
            importance = (final_keywords[i][3] + final_keywords[i+1][3])/2
            final_keywords[i][1] -= multicount
            final_keywords[i+1][1] -= multicount

            if final_keywords[i][1] == 0 and final_keywords[i+1][1] == 0:
                final_keywords.pop(i)
                final_keywords.pop(i)
                DoPop = True
            else:
                if final_keywords[i][1] == 0:
                    final_keywords.pop(i)
                    DoPop = True
                elif final_keywords[i + 1][1] == 0:
                    final_keywords.pop(i + 1)
                    DoPop = True

            multikeyword = [multiword, multicount, pos, importance]
            modifiedKeywords.append(multikeyword)
        else :
            modifiedKeywords.append(final_keywords[i])

    if not DoPop:
        i += 1

for word in final_keywords:
    if not word[0] in [x[0] for x in modifiedKeywords] and word[1] is not 0:
        modifiedKeywords.append(word)

print 'modified keywords : ', len(modifiedKeywords), modifiedKeywords
"""

# sorting the keywords
sortedByImportance = sorted(final_keywords, key=operator.itemgetter(3), reverse=True)
print 'Sorting by importance : ', sortedByImportance
sortedByFrequency = sorted(final_keywords, key=operator.itemgetter(1), reverse=True)
print 'Sorting by frequency : ', sortedByFrequency

# Selecting keywords 1 - excepting data whose frequency is zero and importance is 0.01.
selectedKeywords = []
for element in sortedByFrequency:
    if element[1] == 1 and element[3] == 0.01:
        pass
    else:
        selectedKeywords.append(element)

print 'Selected Keywords 1 : ', selectedKeywords

# importance * freqeuncy
weightedKeywords = []
for element in sortedByFrequency:
    weightedImpt = element[1] * element[3]
    weightedKeywords.append([element[0], weightedImpt])

weightedKeywords.sort(key=operator.itemgetter(1), reverse=True)

print 'Weighted Importance Keywords : ', weightedKeywords

# Selecting keywords 2 - selecting data whose importance is more than 0.05. *fail!!!!!!!!*
selectedKeywords = []
for element in weightedKeywords:
    if element[1] > 0.05:
        selectedKeywords.append(element)

print 'Selected Keywords 2 : ', len(selectedKeywords), selectedKeywords
