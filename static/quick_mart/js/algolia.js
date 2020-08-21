const client = algoliasearch('UY79BIGIQN', 'c2f06d5efd2c4e5c17788dc2a566f8c6');
const diet_restrictions = client.initIndex('diet_restrictions');

autocomplete('#aa-search-input', {}, [
    {
      source: autocomplete.sources.hits(diet_restrictions, { hitsPerPage: 3 }),
      displayKey: 'show_name',
      templates: {
        header: '<div class="aa-suggestions-category">Diet Restrictions</div>',
        suggestion({_highlightResult}) {
          return `<span">${_highlightResult.show_name.value}</span>`;
        }
      }
    },
]);

function checkmark_restriction() {
    let diet_restriction = document.getElementById("aa-search-input").value;
    diet_restrictions.getObject(diet_restriction).then(function(result) {
        let element_id = result['form_id'];
        document.getElementById(element_id).checked = true;
        document.getElementById('update').click();
        clearInput();
    });
}

function clearInput() {
    document.getElementById("aa-search-input").value = "";
}