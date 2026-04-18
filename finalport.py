<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pawan Gorad | ENTC Portfolio</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Poppins',sans-serif;
    scroll-behavior:smooth;
}

body{
    background:#020617;
    color:#fff;
    overflow-x:hidden;
}

/* BACKGROUND */
canvas{
    position:fixed;
    top:0;
    left:0;
    z-index:-1;
}

/* NAVBAR */
nav{
    position:fixed;
    width:100%;
    background:rgba(2,6,23,0.7);
    backdrop-filter:blur(10px);
    padding:15px;
    text-align:center;
    z-index:1000;
}

nav a{
    color:#fff;
    margin:0 15px;
    text-decoration:none;
}

/* HOME */
#home{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.home-content{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:60px;
    flex-wrap:wrap;
}

/* PHOTO */
.home-img img{
    width:260px;
    height:260px;
    border-radius:50%;
    object-fit:cover;
    object-position:top;
    border:4px solid #00f7ff;
    box-shadow:0 0 25px #00f7ff;
    animation: float 3s ease-in-out infinite;
}

@keyframes float{
    0%{transform:translateY(0);}
    50%{transform:translateY(-12px);}
    100%{transform:translateY(0);}
}

/* TEXT */
.home-text h1{
    font-size:3rem;
}

.home-text span{
    color:#00f7ff;
    text-shadow:0 0 15px #00f7ff;
}

.typing{
    color:#00f7ff;
}

.btn{
    margin-top:20px;
    display:inline-block;
    padding:12px 30px;
    background:#00f7ff;
    color:#000;
    border-radius:30px;
    text-decoration:none;
    box-shadow:0 0 20px #00f7ff;
    transition:0.3s;
}

.btn:hover{
    transform:scale(1.1);
}

/* SECTIONS */
section{
    padding:90px 20px;
    max-width:1100px;
    margin:auto;
    opacity:0;
    transform:translateY(50px);
    transition:0.6s;
}

section.show{
    opacity:1;
    transform:translateY(0);
}

h2{
    color:#00f7ff;
    text-align:center;
    margin-bottom:30px;
}

/* CARD */
.card{
    background:#0f172a;
    padding:25px;
    border-radius:15px;
    border:1px solid #1e293b;
    box-shadow:0 0 20px #00f7ff30;
}

/* PROJECTS */
.projects{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
}

.project-card{
    background:#0f172a;
    padding:20px;
    border-radius:15px;
    transition:0.3s;
}

.project-card:hover{
    transform:translateY(-10px);
    box-shadow:0 0 30px #00f7ff60;
}

/* SKILLS */
.skills{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
    gap:20px;
}

.skill{
    padding:20px;
    text-align:center;
    border-radius:12px;
    background:#0f172a;
    border:1px solid #00f7ff40;
    color:#00f7ff;
}

/* TIMELINE */
.timeline{
    border-left:3px solid #00f7ff;
    padding-left:20px;
}

.timeline-item{
    margin:20px 0;
}

/* FOOTER */
footer{
    text-align:center;
    padding:20px;
    background:#000;
}
.modal{
    display:none;
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.9);
    justify-content:center;
    align-items:center;
    z-index:2000;
}

/* when active */
.modal:target{
    display:flex;
}

.modal-content{
    max-width:80%;
    max-height:80%;
    border:3px solid #00f7ff;
    border-radius:10px;
    box-shadow:0 0 25px #00f7ff;
}

.close{
    position:absolute;
    top:20px;
    right:30px;
    font-size:40px;
    color:#fff;
    text-decoration:none;
}

</style>
</head>

<body>

<canvas id="bg"></canvas>

<!-- NAV -->
<nav>
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#education">Education</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#training">Training</a>
    <a href="#contact">Contact</a>
</nav>

<!-- HOME -->
<section id="home">
    <div class="home-content">

        <!-- PHOTO LEFT -->
        <div class="home-img">
            <img src="profile.jpg" alt="Pawan Photo">
        </div>

        <!-- TEXT RIGHT -->
        <div class="home-text">
            <h1>Hello, I'm <span>Pawan Gorad</span></h1>
            <p>I am a <span class="typing" id="typing"></span></p>
            <a href="#about" class="btn">About Me</a>
        </div>

    </div>
</section>

<!-- ABOUT -->
<section id="about">
    <h2>About Me</h2>
    <div class="card">
        I am a first-year ENTC student at MITAOE with passion for IoT, embedded systems, and electronics.
    </div>
</section>

<!-- EDUCATION -->
<section id="education">
    <h2>Education</h2>
    <div class="timeline">

        <div class="timeline-item">
            <h3>First-Year ENTC</h3>
            <p>MITAOE</p>
            <p>SGPA: 9.29</p>
        </div>

        <div class="timeline-item">
            <h3>12th HSC</h3>
            <p>89.33%</p>
        </div>

        <div class="timeline-item">
            <h3>10th SSC</h3>
            <p>90.80%</p>
        </div>

    </div>
</section>

<!-- SKILLS -->
<section id="skills">
    <h2>Skills</h2>
    <div class="skills">
        <div class="skill">C</div>
        <div class="skill">Python</div>
        <div class="skill">HTML</div>
        <div class="skill">CSS</div>
        <div class="skill">PCB</div>
    </div>
</section>

<!-- PROJECTS -->
<section id="projects">
    <h2>Projects</h2>
    <div class="projects">

        <div class="project-card">Smart Drone Locator</div>
        <div class="project-card">Radar System</div>
        <div class="project-card">Audio Visualizer</div>
        <div class="project-card">Power Supply</div>

    </div>
</section>

<!-- TRAINING -->
<section id="training">
    <h2>Training & Certifications</h2>
    <div class="timeline">

        <div class="timeline-item">Embedded Systems & IoT</div>
        <div class="timeline-item">Python for IoT</div>
        <div class="timeline-item">Kotak Scholarship</div>

    </div>
</section>

<!-- CONTACT -->
<section id="contact">
    <h2>Contact</h2>
    <p style="text-align:center;">Email: your.email@example.com</p>
</section>

<footer>
    © 2026 Pawan Gorad
</footer>

<script>
// typing effect
const roles=["ENTC Student","IoT Enthusiast","Embedded Developer"];
let i=0,j=0,isDeleting=false;

function type(){
    let text=roles[i];
    document.getElementById("typing").textContent=text.substring(0,j);

    if(!isDeleting){
        j++;
        if(j>text.length){isDeleting=true;}
    }else{
        j--;
        if(j===0){
            isDeleting=false;
            i=(i+1)%roles.length;
        }
    }
    setTimeout(type,100);
}
type();

// scroll animation
const sections=document.querySelectorAll("section");
window.addEventListener("scroll",()=>{
    sections.forEach(sec=>{
        if(window.scrollY>sec.offsetTop-400){
            sec.classList.add("show");
        }
    });
});

// particles
const canvas=document.getElementById("bg");
const ctx=canvas.getContext("2d");
canvas.width=window.innerWidth;
canvas.height=window.innerHeight;

let particles=[];
for(let i=0;i<40;i++){
    particles.push({
        x:Math.random()*canvas.width,
        y:Math.random()*canvas.height,
        r:Math.random()*1.5,
        dx:(Math.random()-0.5)/2,
        dy:(Math.random()-0.5)/2
    });
}

function animate(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    particles.forEach(p=>{
        ctx.beginPath();
        ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
        ctx.fillStyle="#00f7ff";
        ctx.fill();
        p.x+=p.dx;
        p.y+=p.dy;
        if(p.x<0||p.x>canvas.width) p.dx*=-1;
        if(p.y<0||p.y>canvas.height) p.dy*=-1;
    });
    requestAnimationFrame(animate);
}
animate();
</script>
<!-- POPUP MODAL -->
<div id="cert1" class="modal">

    <a href="#awards" class="close">&times;</a>

    <img src="certificates/hashgraph.jpg" class="modal-content" alt="Certificate">

</div>

</body>
</html>
