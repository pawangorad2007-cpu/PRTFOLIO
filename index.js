const roles=["First-Year ENTC Student At MIT Academy Of Engineering","IoT Enthusiast","Electronics Learner"];
let i=0,j=0,current="",isDeleting=false;

function type(){
    current=roles[i];
    if(isDeleting){
        document.getElementById("typing").textContent=current.substring(0,j--);
        if(j<0){isDeleting=false;i=(i+1)%roles.length;}
    }else{
        document.getElementById("typing").textContent=current.substring(0,j++);
        if(j>current.length){isDeleting=true;}
    }
    setTimeout(type,100);
}
type();

const sections=document.querySelectorAll("section");
window.addEventListener("scroll",()=>{
    sections.forEach(sec=>{
        if(window.scrollY>sec.offsetTop-400){
            sec.classList.add("show");
        }
    });
});