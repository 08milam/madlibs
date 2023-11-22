// const cards = document.querySelectorAll('.container')
// event.preventDefault();
// function flipTile(){
//     this.classList.toggle('flip')

//     console.log('clicked')
// }
// cards.forEach(card => card.addEventListener('onsubmit', flipTile))




function flipElement(event) {
    event.preventDefault();

    const flipElement = document.querySelector('.container');
    flipElement.style.transform = flipElement.style.transform === 'rotateY(180deg)' ? 'rotateY(0deg)' : 'rotateY(180deg)';
  }

