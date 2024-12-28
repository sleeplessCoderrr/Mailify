<script>
    export let isVisible = false; // Controls the visibility of the modal
    export let title = "Error";
    export let message = "Something went wrong.";

    function closeModal() { isVisible = false; }
</script>

{#if isVisible}
    <div class="fixed inset-0 bg-midnight bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white rounded-lg shadow-lg p-6 max-w-sm w-full text-center">
            <h2 class="text-lg font-bold text-midnight">{title}</h2>
            <p class="text-sm text-midnight mt-2">{message}</p>
            <button on:click={closeModal} class="mt-4 px-4 py-2 bg-blaze/70 text-white rounded-md hover:bg-blaze transition duration-300">
                OK
            </button>
        </div>
    </div>
{/if}
