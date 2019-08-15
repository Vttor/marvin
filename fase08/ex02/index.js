var arr=[]
function clique(){
    var array=["http://s2.glbimg.com/4Ek8CnZSuYyyvaNQEPPiX_d-faA=/e.glbimg.com/og/ed/f/original/2017/11/24/gali1.jpg","https://image-store.slidesharecdn.com/854e3f8c-a948-4051-b3fa-574fe160e36c-original.png","https://scontent-atl3-1.cdninstagram.com/vp/5052ceac7760e90369e146133c7e95c1/5DA3B04F/t51.2885-19/s150x150/56842918_368472680544650_8641758371768172544_n.jpg?_nc_ht=scontent-atl3-1.cdninstagram.com","https://media-manager.noticiasaominuto.com/1920/1552648327/naom_59b7f11a381ff.jpg?crop_params=eyJwb3J0cmFpdCI6eyJjcm9wV2lkdGgiOjcxOCwiY3JvcEhlaWdodCI6MTA3OSwiY3JvcFgiOjYwMywiY3JvcFkiOjB9LCJsYW5kc2NhcGUiOnsiY3JvcFdpZHRoIjoxOTE3LCJjcm9wSGVpZ2h0IjoxMDc5LCJjcm9wWCI6MCwiY3JvcFkiOjB9fQ==","https://img.estadao.com.br/thumbs/640/resources/jpg/0/4/1512053836140.jpg","https://i1.wp.com/petanjo.com/blog/wp-content/uploads/2014/09/gato-te-ama.png?fit=990%2C500&ssl=1"]
    var x = Math.floor(Math.random()*6)
    if(arr.indexOf(x)!=-1){
        if(arr.lenght==6){
            arr.splice(0,6)
            clique()
        }
        else{
            clique()
        }
    }
    else{
        
        arr.push(x)
        document.getElementById("1").src = array[x]
    }
    
}