class summary:
    def __init__(self, content):
        if content is not None:
           self.data = content
        else:
            self.data = "None"

    def getsummary(self):
        return self.data


if __name__ == '__main__':
    print(summary("""A newspaper is a periodical publication containing written information about current events and is often typed in black ink with a white or gray background.

Newspapers can cover a wide variety of fields such as politics, business, sports and art, and often include materials such as opinion columns, weather forecasts, reviews of local services, obituaries, birth notices, crosswords, editorial cartoons, comic strips, and advice columns.

Most newspapers are businesses, and they pay their expenses with a mixture of subscription revenue, newsstand sales, and advertising revenue. The journalism organizations that publish newspapers are themselves often metonymically called newspapers.

Newspapers have traditionally been published in print (usually on cheap, low-grade paper called newsprint). However, today most newspapers are also published on websites as online newspapers, and some have even abandoned their print versions entirely.

Newspapers developed in the 17th century, as information sheets for merchants. By the early 19th century, many cities in Europe, as well as North and South America, published newspapers.

Some newspapers with high editorial independence, high journalism quality, and large circulation are viewed as newspapers of record.

With the advent of the internet many newspapers are now digital, with their news presented online rather than in a physical format, with there now being a decline in sales for paper copies of newspapers.""").getsummary())