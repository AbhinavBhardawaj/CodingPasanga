let startTime = Date.now();
window.addEventListener('beforeunload',function(){
    let endTime = Date.now();
    let timeSpent = Math.round((endTime-startTime)/60000);

    navigator.sendBeacon('/track-time/',JSON.stringify({'minutes':timeSpent}));
    
});