$(document).ready(function () {
	$('.toast').toast('show');
});

function modalLoader(params) {
	var modalCaller = '.modalCaller';
	var url = modalCaller.data('url');
	var size = modalCaller.data('size');

	var modal = $('#generalModal');
	var modalHeader = $('#generalModal #modalHeader');
	var modalContent = $('#generalModal #modalContent');
	var modalFooter = $('#generalModal #modalFooter');
	modal.modal('show');
}
