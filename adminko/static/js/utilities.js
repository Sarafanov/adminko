function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            document.getElementById('imgPreview').src = e.target.result;
        }

        reader.readAsDataURL(input.files[0]);
    }
}

function cut_long_ref_names() {
    links = document.getElementsByClassName('product-box-dsc-ref')
    for (var i = 0; i < links.length; i++) {
        s = links[i].innerHTML;
        if (s.length > 24) {
            s = s.substring(0, 23) + '...';
            links[i].innerHTML = s;
        }
    }
}

window.onload = function () {
    cut_long_ref_names();
};
