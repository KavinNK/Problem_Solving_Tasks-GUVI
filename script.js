function getNewsApi() {
  var Section = document.getElementById("section").value
  var url ="https://api.nytimes.com/svc/topstories/v2/"+Section+".json?api-key=GgJGkGCqaCoFTCOnxoAkAaGj7ADjER5V";
  const options = {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  };
  fetch(url, options)
    .then((response) => {
      if (response.ok) {

        return response.text();
      }
      return response.text().then((err) => {
        return Promise.reject({
          status: response.status,
          statusText: response.statusText,
          errorMessage: err,
        });
      });
    })
    .then((data) => {
        var Data = JSON.parse(data)
    try{
        for(i=0;i<Data.results.length;i++) {
            var Abstract = Data.results[i].abstract
            var Title = Data.results[i].title
            var Byline = Data.results[i].byline
            var Type = Data.results[i].item_type
            var Section = Data.results[i].section
            var Date = Data.results[i].updated_date
            Date = Date.slice(0, 10);
            var ShortUrl = Data.results[i].short_url
            var imgUrl = Data.results[i].multimedia[4].url
    
        console.log(i)
        console.log("1.Abstract :"+Abstract)
        console.log("2.Title :"+title)
        console.log("3.Byline :"+Byline)
        console.log("4.Type :"+Type)
        console.log("5.Section :"+Section)
        console.log("6.Date :"+Date)
        console.log("7.ShortUrl :"+ShortUrl)
        console.log("8.imgUrl :"+imgUrl)
        debugger
        const Main=document.getElementById("root")
        var displaycard=document.createElement('div')
        displaycard.classList.add("card")
        var Row = document.createElement("div")
        Row.classList.add("row")
        var ColLeft = document.createElement("div")
        ColLeft.classList.add("col-sm-8")
        ColLeft.id="colLeft"
        var ColRight = document.createElement("div")
        ColRight.classList.add("col-sm-4")
        ColRight.id="colRight"
        var imageUrl = document.createElement('img')
        imageUrl.src=imgUrl
        imageUrl.style.width="100%"
        imageUrl.style.height="100%"
        imageUrl.style.objectFit="contain"


        var section = document.createElement('h3')
        section.style.color="blue"

        section.innerText ="Section : "+Section

        var title = document.createElement('h3')
        title.innerText = Title
        
        var date = document.createElement('p')
        date.style.color="grey"
        date.innerText = Date

        var abstract = document.createElement('p')
        abstract.style.color="grey"
        abstract.innerText = Abstract

        var byline = document.createElement('p')
        byline.style.color="black"
        byline.innerText = Byline
        var shortUrl = document.createElement('a')
        shortUrl.href=ShortUrl
        shortUrl.target="_blank"
        shortUrl.innerText="Continue Reading"













        Main.appendChild(displaycard)
        displaycard.appendChild(Row)
        Row.appendChild(ColLeft)
        Row.appendChild(ColRight)
        ColLeft.appendChild(section)
        ColLeft.appendChild(title)
        ColLeft.appendChild(date)
        ColLeft.appendChild(abstract)
        ColLeft.appendChild(byline)
        ColLeft.appendChild(shortUrl)
        ColRight.appendChild(imageUrl)

       
        }
    }
     catch(e){
         console.log(e)
     }

    })
    .catch((err) => {
      console.error(err);
    });
}
