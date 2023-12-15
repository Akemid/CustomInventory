const {createApp, ref} = Vue
import mitt from 'mitt'
const emitter = mitt()

createApp(
    {
    setup(){
        const classAttributep = ref('')
        const classBsToggle = ref('')
        const editMode = ref(false)
        function setClassAttribute(){
            if (editMode.value == true)
            {
                classAttributep.value = '#editProductModal'
            }
            else {
                classAttributep.value = '#addProductModal'
            }
        }
        function addCategoryModal(pEditMode){
            console.log("addCategoryModal:",pEditMode)
            editMode.value = pEditMode
            classBsToggle.value = 'modal'
            setClassAttribute()
        }
 

        return {
            editMode,
            classAttributep,
            addCategoryModal,
            classBsToggle,
        }
    },
    delimiters : ['${','}']}    
).provide('emitter', emitter).mount('#modals')

// createApp(
//     {
//     setup(){
//         const classAttributep = ref('')
//         const a = ref(false)
//         function addCategory(){
//              console.log("addCategory")
//             }       
        
//         return {
//             addCategory
//         }
//     },
//     delimiters : ['${','}']
//     }
// ).mount('#addCategoryModal')


