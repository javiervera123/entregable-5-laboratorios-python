
document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("nav-toggle");
  const nav = document.querySelector(".nav-contenedor");

  // 👉 Abrir / cerrar menú hamburguesa
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("active");
    btn.setAttribute("aria-expanded", open);
  });

  // 👉 Cerrar menú cuando se hace clic en un enlace
  document.querySelectorAll(".nav-contenedor a").forEach(link => {
    link.addEventListener("click", () => {
      nav.classList.remove("active");
      btn.setAttribute("aria-expanded", false);
    });
  });
});