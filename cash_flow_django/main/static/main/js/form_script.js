// Функция для обновления категорий
function updateCategories(typeId, selectedCategoryId = null, selectedSubcategoryId = null) {
    var CategoryField = document.getElementById('id_category');
    var SubCategoryField = document.getElementById('id_subcategory');

    if (typeId) {
        CategoryField.disabled = false;

        // Отправляем AJAX запрос для получения категорий
        fetch(`${urls.getCategories}?type_id=${typeId}`)
            .then(response => response.json())
            .then(data => {
                CategoryField.innerHTML = '<option value="">---------</option>';
                // Добавляем новые категории
                data.categories.forEach(function(category) {
                    var option = document.createElement('option');
                    option.value = category.id;
                    option.textContent = category.name;
                    CategoryField.appendChild(option);
                });

                // Если категория была выбрана ранее, восстанавливаем выбор
                if (selectedCategoryId) {
                    CategoryField.value = selectedCategoryId;
                    // После восстановления категории, обновляем подкатегории
                    updateSubcategories(selectedCategoryId, selectedSubcategoryId);
                }
            });
    } else {
        // Если тип не выбран, блокируем поле подкатегории и категории
        DisabledSubCategory(SubCategoryField);
        CategoryField.disabled = true;
        CategoryField.innerHTML = '<option value="">Выберите тип</option>';
    }
}

// Функция для обновления подкатегорий
function updateSubcategories(categoryId, selectedSubcategoryId = null) {
    var subcategoryField = document.getElementById('id_subcategory');

    if (categoryId) {
        subcategoryField.disabled = false;

        // Отправляем AJAX запрос для получения подкатегорий
        fetch(`${urls.getSubcategories}?category_id=${categoryId}`)
            .then(response => response.json())
            .then(data => {
                subcategoryField.innerHTML = '<option value="">---------</option>';
                // Добавляем новые подкатегории
                data.subcategories.forEach(function(subcategory) {
                    var option = document.createElement('option');
                    option.value = subcategory.id;
                    option.textContent = subcategory.name;
                    subcategoryField.appendChild(option);
                });

                // Если подкатегория была выбрана ранее, восстанавливаем выбор
                if (selectedSubcategoryId) {
                    subcategoryField.value = selectedSubcategoryId;
                }
            });
    } else {
        // Если категория не выбрана, блокируем поле подкатегории
        DisabledSubCategory(subcategoryField);
    }
}

// Блокировка подкатегории
function DisabledSubCategory(subcategoryField) {
    subcategoryField.disabled = true;
    if (subcategoryField.tagName === 'SELECT') {
        // Для поля Select модели CashFlowRecord
        subcategoryField.innerHTML = '<option value="">Выберите категорию</option>';
    } else if (subcategoryField.tagName === 'INPUT' && subcategoryField.type === 'text') {
        // Для поля TextInput модели SubCategory
        subcategoryField.value = '';
        subcategoryField.placeholder = 'Выберите категорию';
    }
}

// Когда изменяется категория
document.getElementById('id_category').addEventListener('change', function() {
    var categoryId = this.value;
    var selectedSubcategoryId = document.getElementById('id_subcategory').value;
    updateSubcategories(categoryId, selectedSubcategoryId);
});

// Когда изменяется тип
document.getElementById('id_type').addEventListener('change', function() {
    var typeId = this.value;
    var subcategoryField = document.getElementById('id_subcategory');
    DisabledSubCategory(subcategoryField);
    updateCategories(typeId);
});

// Инициализация на загрузку страницы
document.addEventListener('DOMContentLoaded', function () {
    var categoryId = document.getElementById('id_category').value;
    var typeId = document.getElementById('id_type').value;
    var selectedSubcategoryId = document.getElementById('id_subcategory').value;
    updateCategories(typeId, categoryId, selectedSubcategoryId);
});