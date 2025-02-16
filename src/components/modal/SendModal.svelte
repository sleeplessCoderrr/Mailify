<script lang="ts">
    export let isVisible = false;
    export let title = "Send Email";
    export let message = "Choose your preferred email service:";
    export let onOutlook = () => {};
    export let onGmail = () => {};

    function handleOutlook() {
        onOutlook();
        isVisible = false;
    }

    function handleGmail() {
        onGmail();
        isVisible = false;
    }
</script>

{#if isVisible}
    <div class="fixed inset-0 bg-midnight bg-opacity-50 flex items-center justify-center z-50">
        <div class="bg-white rounded-lg shadow-lg p-6 w-3/12 h-1/4 text-center flex-col justify-evenly items-center">
            <h2 class="text-lg font-bold mt-8 text-midnight">{title}</h2>
            <p class="text-sm text-midnight mt-4">{message}</p>
            <div class="flex justify-around mt-10">
                <button on:click={handleOutlook} class="px-4 py-2 bg-blaze/90 text-white rounded-md hover:bg-blaze transition duration-300">
                    Send with Outlook
                </button>
                <button on:click={handleGmail} class="px-4 py-2 bg-blaze/80 text-white rounded-md hover:bg-blaze transition duration-300">
                    Send with Gmail
                </button>
            </div>
        </div>
    </div>
{/if}
