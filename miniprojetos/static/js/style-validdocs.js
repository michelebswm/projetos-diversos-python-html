function ativaFormularioCpf() {
	const contentCpf = document.querySelector(".content-item-cpf");
	if (contentCpf.style.maxHeight) {
		contentCpf.style.maxHeight = null;
	} else {
		contentCpf.style.maxHeight = contentCpf.scrollHeight + "px";
	}
}

function ativaFormularioCnpj() {
	const contentCnpj = document.querySelector(".content-item-cnpj");
	if (contentCnpj.style.maxHeight) {
		contentCnpj.style.maxHeight = null;
	} else {
		contentCnpj.style.maxHeight = contentCnpj.scrollHeight + "px";
	}
}

function ativaFormularioPis() {
	const contentPis = document.querySelector(".content-item-pis");
	if (contentPis.style.maxHeight) {
		contentPis.style.maxHeight = null;
	} else {
		contentPis.style.maxHeight = contentPis.scrollHeight + "px";
	}
}

function ativaFormularioCnh() {
	const contentCnh = document.querySelector(".content-item-cnh");
	if (contentCnh.style.maxHeight) {
		contentCnh.style.maxHeight = null;
	} else {
		contentCnh.style.maxHeight = contentCnh.scrollHeight + "px";
	}
}

function ativaFormularioTitulo() {
	const contentTitulo = document.querySelector(".content-item-titulo");
	if (contentTitulo.style.maxHeight) {
		contentTitulo.style.maxHeight = null;
	} else {
		contentTitulo.style.maxHeight = contentTitulo.scrollHeight + "px";
	}
}

function ativaFormularioRenavam() {
	const contentRenavam = document.querySelector(".content-item-renavam");
	if (contentRenavam.style.maxHeight) {
		contentRenavam.style.maxHeight = null;
	} else {
		contentRenavam.style.maxHeight = contentRenavam.scrollHeight + "px";
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
