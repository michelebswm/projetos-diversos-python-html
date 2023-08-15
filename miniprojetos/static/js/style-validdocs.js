function ativaFormularioCpf() {
	const contentCpf = document.querySelector(".content-item-cpf");
	if (
		contentCpf.style.display === "none" ||
		contentCpf.style.display === ""
	) {
		contentCpf.style.display = "block";
	} else {
		contentCpf.style.display = "none";
	}
}

function ativaFormularioCnpj() {
	const contentCnpj = document.querySelector(".content-item-cnpj");

	if (
		contentCnpj.style.display === "none" ||
		contentCnpj.style.display === ""
	) {
		contentCnpj.style.display = "block";
	} else {
		contentCnpj.style.display = "none";
	}
}

function ativaFormularioPis() {
	const contentPis = document.querySelector(".content-item-pis");

	if (
		contentPis.style.display === "none" ||
		contentPis.style.display === ""
	) {
		contentPis.style.display = "block";
	} else {
		contentPis.style.display = "none";
	}
}

function ativaFormularioCnh() {
	const contentCnh = document.querySelector(".content-item-cnh");

	if (
		contentCnh.style.display === "none" ||
		contentCnh.style.display === ""
	) {
		contentCnh.style.display = "block";
	} else {
		contentCnh.style.display = "none";
	}
}

function ativaFormularioTitulo() {
	const contentTitulo = document.querySelector(".content-item-titulo");

	if (
		contentTitulo.style.display === "none" ||
		contentTitulo.style.display === ""
	) {
		contentTitulo.style.display = "block";
	} else {
		contentTitulo.style.display = "none";
	}
}

function ativaFormularioRenavam() {
	const contentRenavam = document.querySelector(".content-item-renavam");

	if (
		contentRenavam.style.display === "none" ||
		contentRenavam.style.display === ""
	) {
		contentRenavam.style.display = "block";
	} else {
		contentRenavam.style.display = "none";
	}
}

const btn_cpf = document.getElementById("item-cpf");
btn_cpf.addEventListener("click", ativaFormularioCpf);

const btn_cnpj = document.getElementById("item-cnpj");
btn_cnpj.addEventListener("click", ativaFormularioCnpj);

const btn_pis = document.getElementById("item-pis");
btn_pis.addEventListener("click", ativaFormularioPis);

const btn_cnh = document.getElementById("item-cnh");
btn_cnh.addEventListener("click", ativaFormularioCnh);

const btn_titulo = document.getElementById("item-titulo");
btn_titulo.addEventListener("click", ativaFormularioTitulo);

const btn_renavam = document.getElementById("item-renavam");
btn_renavam.addEventListener("click", ativaFormularioRenavam);
