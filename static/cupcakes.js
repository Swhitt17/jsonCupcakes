// const BASE_URL = "http://127.0.0.1:5000/api"

function makeCupcakeHTML(cupcake){
    return `
    <div data-cupcake-id=${cupcake.id}>
    <li>
    ${cupcake.flavor}/${cupcake.size}/${cupcake.rating}
    <button class="delete-button">X</button>
    </li>
    <img class="Cupcake-img"
         src="${cupcake.image}"
         alt="(no image provided)">
    </div>
    `;

}


async function getCupcakes(){
    const res = await axios.get("http://127.0.0.1:5000/api/cupcakes")

for(let cupcakeData of res.data.cupcakes) {
    let newCupcake = $(makeCupcakeHTML(cupcakeData));
    $("#cupcakes-list").append(newCupcake);
}

}


$("#cupcake-form").on("submit", async function(e){
e.preventDefault();

let flavor = $("#f-flavor").val();
let size = $("#f-size").val();
let rating = $("#f-rating").val();
let image = $("#f-image").val();

const newCupcakeRes = await axios.post("http://127.0.0.1:5000/api/cupcakes",{
    flavor,
    size,
    rating,
    image
});

let newCupcake = $(makeCupcakeHTML(newCupcakeRes.data.cupcake));
$("#cupcakes-list").append(newCupcake);
$("#cupcake-form").trigger("reset");

});

$("#cupcakes-list").on("click",".delete-button", async function(e){
e.preventDefault();

let $cupcake = $(e.target).closest("div");
let cupcakeId = $cupcake.attr("data-cupcake-id");

await axios.delete(`http://127.0.0.1:5000/api/cupcakes/${cupcakeId}`);
$cupcake.remove();

});



$(getCupcakes);