document.getElementById("form1").onsubmit=function() {
    style = parseInt(document.querySelector('input[name = "style"]:checked').value);
    food = parseInt(document.querySelector('input[name = "food"]:checked').value);
    member = parseInt(document.querySelector('input[name = "member"]:checked').value);
    activity = parseInt(document.querySelector('input[name = "activity"]:checked').value);

    result = style + food + member + activity;  //calculate total, add points together

    document.getElementById("grade").innerHTML = result;
    //display member's name and picture after clicked submit button
    if (result == 4, 5, 6) {result2 = "Jisoo<br /><img src='/static/assets/jisoo.jpeg/' width='300' />"}; //if total point is between 4 and 6, you are jisoo
    if (result == 7, 8, 9) {result2 = "Jennie<br /><img src='/static/assets/jennie.jpg/' width='300' />"}; //if total point is between 7 and 9, you are jennie
    if (result == 10, 11, 12) {result2 = "Rose<br /><img src='/static/assets/rose.jpg/' width='300' />"}; //if total point is between 10 and 12, you are rose
    if (result == 13, 14, 15, 16) {result2 = "Lisa<br /><img src='/static/assets/lisa.jpg/' width='300' />"}; //if total point is between 13 and 16, you are lisa
    document.getElementById("grade2").innerHTML = result2;


    return false; // required to not refresh the page; just leave this here
} //this ends the submit function

//random BLACKPINK facts
var facts = [
    'In 2016, YG Entertainment revealed that the reason BLACKPINK was chosen was to dismantle the idea that the color “pink” is only used to portray prettiness or cuteness. With this new group of girls, they wanted to show that pink doesn’t just mean “pretty,” but also incredible talent and hard work.',
    'Jisoo is crazy for Pikachu.',
    'Lisa was so good that when she auditioned for YG in Thailand in 2010, she not only won first place but also beat out all of the competition. She ended up being the only candidate selected by the label at the time, as well as the first non-Korean artist to work at YG.',
    'BLACKPINK have their own reality TV show called BLACKPINK House, which follows the daily lives of the girls with a little bit of YG spice thrown in.',
    'BLACKPINK has BLINKS. A clever combination of Black and Pink, BLINKs are responsible for continually helping the girl group break records, especially on YouTube. For example, their smash hit Ddu-Du Ddu-Du garnered 36.2 million views in its first 24 hours.',
    'BLACKPINK was originally supposed to have 9 members. Interestingly enough, one of those cut trainees was none other than (G)I-DLE’s Miyeon!' ,
    'BLACKPINK has also been able to make big moves on the global stage, thanks to the unique background of each member. For example, Rosé was born in New Zealand and grew up in Australia, while Jennie went to school in New Zealand for a number of years. Lisa grew up in Thailand, and Jisoo was raised in South Korea.',
    'Between the 4 members, they can speak a number of languages besides Korean, like Japanese, English, Thai, and Mandarin. These language skills allow them to interact with more fans in more countries.',
    'BLACKPINK’s new single Kill This Love just casually beat out Ariana Grande’s thank u, next for the most views for a music video debut on YouTube within 24 hours, which was 56.7 MILLION VIEWS.',
    'Lisa’s step-father is none other than Marco Bruschweiler, a Master Chef and member of The World Association of Chefs’ Societies. He seems to be very supportive of Lisa, and has even made an appearance on BLACKPINK House, which moved Lisa to tears.'
]

function newFact() {
    var randomNumber = Math.floor(Math.random() * (facts.length));
    document.getElementById('factDisplay').innerHTML = facts[randomNumber];
}

//click button to display BLACKPINK mv
function displayVideo() {
    if($('#display-video').css('display') === 'none') $('#display-video').css('display', 'block')
    else $('#display-video').css('display', 'none')
}
function displayVideo2() {
    if($('#display-video2').css('display') === 'none') $('#display-video2').css('display', 'block')
    else $('#display-video2').css('display', 'none')
}
function displayVideo3() {
    if($('#display-video3').css('display') === 'none') $('#display-video3').css('display', 'block')
    else $('#display-video3').css('display', 'none')
}

//click button to change header image
function changeImage() {
    console.log("hi")
    document.getElementById("header").style.backgroundImage = 'url("/static/assets/blackpink (1).jpg")'
}
function changeImage2() {
    console.log("hi")
    document.getElementById("header").style.backgroundImage = 'url("/static/assets/blackpink3.jpg")'
}
function changeImage3() {
    console.log("hi")
    document.getElementById("header").style.backgroundImage = 'url("/static/assets/blackpink4.jpg")'
}
function changeImage4() {
    console.log("hi")
    document.getElementById("header").style.backgroundImage = 'url("/static/assets/blackpink6.jpg")'
}
