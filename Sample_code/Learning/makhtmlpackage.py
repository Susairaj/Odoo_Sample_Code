import makeHTML
pageTitle = 'Hello World'
pageHead = makeHTML.part('head')
pageHead.addPart('title', content=pageTitle)
pageBody = makeHTML.part('body')
pageBody.addPart('h1', content=pageTitle)
pageBody.addPart('p', content="Oh no, not again!")
pageBody.addPart('hr')
links ='google.com'
page_url = makeHTML.linkedList('href')
page_url.addLinks(links)
fullPage = makeHTML.part('html')
fullPage.addPiece(pageHead)
fullPage.addPiece(pageBody)
fullPage.addPiece(page_url)
print fullPage.make()
