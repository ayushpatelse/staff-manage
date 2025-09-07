window.addEventListener('DOMContentLoaded', ()=>{
    const signal_help_text = document.querySelectorAll('.signal-box-help-text');
    let activeElement = null;
    
    signal_help_text.forEach(box=>{
        
        box.addEventListener('click',(event)=>{
            
            const clickedBox = event.target;
            const helpBox = clickedBox.nextElementSibling;
            const helpBoxText = clickedBox.dataset.statusText;

            console.log("active=>", ((activeElement!=null)?activeElement.classList:null));
            console.log("clicked=>", clickedBox.classList);
            console.log("helpBox=>",helpBox);
            console.log("helpBoxText=>",helpBoxText);
            
            if ( activeElement && activeElement != clickedBox )
                {
                    const activeHelpTextSpan = activeElement.nextElementSibling;
                    if(activeHelpTextSpan &&  activeHelpTextSpan.classList.contains('show')){
                    activeHelpTextSpan.classList.remove('show');
                    activeHelpTextSpan.classList.add('hidden');
                }
                
            }
            
            if (helpBox.classList.contains('show')){
                
                helpBox.classList.remove('show');
                helpBox.classList.add('hidden');
                activeElement = null;
                console.log('show remove');
            }
            else{
                helpBox.textContent = helpBoxText;
                helpBox.classList.remove('hidden');
                helpBox.classList.add('show');
                activeElement = clickedBox;
                console.log('show add');
            }
            console.log("active=>", ((activeElement!=null)?activeElement.classList:null));
            console.log("----------------------------------------------------------------");

        })
    });

        
    
})

