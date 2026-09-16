document.querySelectorAll('.thoughts-list details').forEach(function (thought) {
  var summary = thought.querySelector('summary');
  var pinned = false;
  var hovered = false;
  var focused = false;

  function update() {
    thought.open = pinned || hovered || focused;
  }

  thought.addEventListener('pointerenter', function (event) {
    if (event.pointerType === 'mouse') {
      hovered = true;
      update();
    }
  });
  thought.addEventListener('pointerleave', function () {
    hovered = false;
    update();
  });
  summary.addEventListener('focus', function () {
    focused = true;
    update();
  });
  summary.addEventListener('blur', function () {
    focused = false;
    update();
  });
  summary.addEventListener('click', function (event) {
    event.preventDefault();
    pinned = !pinned;
    focused = false;
    hovered = false;
    update();
  });
  thought.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
      pinned = hovered = focused = false;
      update();
    }
  });
});
