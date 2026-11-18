
const contentForm = document.querySelector("#contentForm");
const contentId = document.querySelector("#contentId");
const contentTitle = document.querySelector("#contentTitle");
const platform = document.querySelector("#platform");
const format = document.querySelector("#format");
const publishDate = document.querySelector("#publishDate");
const contentStatus = document.querySelector("#contentStatus");
const contentDescription = document.querySelector("#contentDescription");

const contentList = document.querySelector("#contentList");
const emptyState = document.querySelector("#emptyState");

const searchInput = document.querySelector("#searchInput");
const filterStatus = document.querySelector("#filterStatus");
const filterPlatform = document.querySelector("#filterPlatform");

const submitBtn = document.querySelector("#submitBtn");
const cancelEdit = document.querySelector("#cancelEdit");

let posts = [];

const platformIcons = {
    Instagram: "📸",
    TikTok: "🎵",
    Facebook: "🔵",
    YouTube: "▶️",
    LinkedIn: "💼",
    Otra: "🌐"
};

const statusNames = {
    idea: "Idea",
    planned: "Planificado",
    published: "Publicado"
};


// GUARDAR LOS DATOS

function savePosts() {

    localStorage.setItem("ideaSpacePosts", JSON.stringify(posts));

}


// CARGAR LOS DATOS

function loadPosts() {

    let savedPosts = localStorage.getItem("ideaSpacePosts");

    if (savedPosts !== null) {

        try {

            let parsedPosts = JSON.parse(savedPosts);

            posts = Array.isArray(parsedPosts) ? parsedPosts : [];

        } catch (error) {

            posts = [];

        }

    }

    renderPosts();

}


// CREAR UN NUEVO CONTENIDO

function addPost(event) {

    event.preventDefault();

    let title = contentTitle.value.trim();

    if (title === "") {

        alert("Escribe un nombre para el contenido.");

        return;

    }

    let postData = {

        title: title,
        platform: platform.value,
        format: format.value,
        date: publishDate.value,
        status: contentStatus.value,
        description: contentDescription.value.trim()

    };


    if (contentId.value !== "") {

        let post = posts.find(function(item) {

            return String(item.id) === contentId.value;

        });

        if (post) {

            post.title = postData.title;
            post.platform = postData.platform;
            post.format = postData.format;
            post.date = postData.date;
            post.status = postData.status;
            post.description = postData.description;

        }

    } else {

        let newPost = {

            id: Date.now().toString(),
            ...postData

        };

        posts.push(newPost);

    }

    savePosts();

    resetForm();

    renderPosts();

}


// MOSTRAR LOS CONTENIDOS

function renderPosts() {

    contentList.replaceChildren();

    let filteredPosts = posts.filter(function(post) {

        let search = searchInput.value.toLowerCase();

        let matchesSearch =
            post.title.toLowerCase().includes(search) ||
            post.description.toLowerCase().includes(search);

        let matchesStatus =
            filterStatus.value === "all" ||
            post.status === filterStatus.value;

        let matchesPlatform =
            filterPlatform.value === "all" ||
            post.platform === filterPlatform.value;

        return matchesSearch && matchesStatus && matchesPlatform;

    });


    filteredPosts.sort(function(a, b) {

        if (!a.date) return 1;

        if (!b.date) return -1;

        return a.date.localeCompare(b.date);

    });


    emptyState.hidden = filteredPosts.length !== 0;

    contentList.hidden = filteredPosts.length === 0;


    filteredPosts.forEach(function(post) {

        let card = document.createElement("article");

        card.className = "content-card";


        let cardTop = document.createElement("div");

        cardTop.className = "card-top";


        let platformBadge = document.createElement("span");

        platformBadge.className = "platform-chip";

        platformBadge.textContent =
            platformIcons[post.platform] + " " + post.platform;


        let statusBadge = document.createElement("span");

        statusBadge.className = "status-badge status-" + post.status;

        statusBadge.textContent = statusNames[post.status];


        cardTop.appendChild(platformBadge);

        cardTop.appendChild(statusBadge);


        let title = document.createElement("h3");

        title.textContent = post.title;


        let description = document.createElement("p");

        description.className = "card-description";

        description.textContent =
            post.description || "Sin descripción añadida.";


        let cardBottom = document.createElement("div");

        cardBottom.className = "card-bottom";


        let formatText = document.createElement("span");

        formatText.textContent = "✧ " + post.format;


        let dateText = document.createElement("span");

        dateText.textContent = post.date
            ? new Date(post.date + "T00:00:00").toLocaleDateString("es-ES")
            : "Sin fecha";


        cardBottom.appendChild(formatText);

        cardBottom.appendChild(dateText);


        let actions = document.createElement("div");

        actions.className = "card-actions";


        let publishButton = document.createElement("button");

        publishButton.type = "button";

        publishButton.className = "action-publish";

        publishButton.textContent =
            post.status === "published"
                ? "↶ Volver a planificado"
                : "✓ Marcar publicado";


        publishButton.addEventListener("click", function() {

            changeStatus(post.id);

        });


        let editButton = document.createElement("button");

        editButton.type = "button";

        editButton.className = "action-edit";

        editButton.textContent = "✎ Editar";


        editButton.addEventListener("click", function() {

            editPost(post.id);

        });


        let deleteButton = document.createElement("button");

        deleteButton.type = "button";

        deleteButton.className = "action-delete";

        deleteButton.textContent = "✕ Eliminar";


        deleteButton.addEventListener("click", function() {

            deletePost(post.id);

        });


        actions.appendChild(publishButton);

        actions.appendChild(editButton);

        actions.appendChild(deleteButton);


        card.appendChild(cardTop);

        card.appendChild(title);

        card.appendChild(description);

        card.appendChild(cardBottom);

        card.appendChild(actions);


        contentList.appendChild(card);

    });


    updateDashboard();

}


// CAMBIAR EL ESTADO

function changeStatus(id) {

    let post = posts.find(function(item) {

        return item.id === id;

    });

    if (post) {

        if (post.status === "published") {

            post.status = "planned";

        } else {

            post.status = "published";

        }

        savePosts();

        renderPosts();

    }

}


// EDITAR CONTENIDO

function editPost(id) {

    let post = posts.find(function(item) {

        return item.id === id;

    });

    if (!post) return;


    contentId.value = post.id;

    contentTitle.value = post.title;

    platform.value = post.platform;

    format.value = post.format;

    publishDate.value = post.date;

    contentStatus.value = post.status;

    contentDescription.value = post.description;


    submitBtn.textContent = "Guardar cambios";

    cancelEdit.hidden = false;


    document.querySelector("#crear").scrollIntoView({

        behavior: "smooth"

    });

}


// ELIMINAR CONTENIDO

function deletePost(id) {

    let confirmDelete = confirm(
        "¿Estás segura de que quieres eliminar este contenido?"
    );

    if (confirmDelete) {

        posts = posts.filter(function(post) {

            return post.id !== id;

        });

        savePosts();

        renderPosts();

    }

}


// ACTUALIZAR LOS CONTADORES

function updateDashboard() {

    let total = posts.length;


    let planned = posts.filter(function(post) {

        return post.status !== "published";

    }).length;


    let published = posts.filter(function(post) {

        return post.status === "published";

    }).length;


    let currentDate = new Date();

    let today = currentDate.getFullYear() + "-" +
        String(currentDate.getMonth() + 1).padStart(2, "0") + "-" +
        String(currentDate.getDate()).padStart(2, "0");


    let upcoming = posts.filter(function(post) {

        return post.date &&
            post.date >= today &&
            post.status !== "published";

    }).length;


    document.querySelector("#totalCount").textContent = total;

    document.querySelector("#plannedCount").textContent = planned;

    document.querySelector("#publishedCount").textContent = published;

    document.querySelector("#upcomingCount").textContent = upcoming;

}


// LIMPIAR EL FORMULARIO

function resetForm() {

    contentForm.reset();

    contentId.value = "";

    submitBtn.textContent = "+ Guardar contenido";

    cancelEdit.hidden = true;

}


// EVENTOS DEL FORMULARIO

contentForm.addEventListener("submit", addPost);


cancelEdit.addEventListener("click", function() {

    resetForm();

});


// EVENTOS DE LOS FILTROS

searchInput.addEventListener("input", renderPosts);

filterStatus.addEventListener("change", renderPosts);

filterPlatform.addEventListener("change", renderPosts);


// MOSTRAR LA FECHA ACTUAL

function showToday() {

    let today = new Date();

    let options = {

        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric"

    };

    let date = today.toLocaleDateString("es-ES", options);

    document.querySelector("#todayLabel").textContent = date;

}


// INICIAR LA APLICACIÓN

showToday();

loadPosts();

