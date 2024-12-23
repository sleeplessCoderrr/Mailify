<script>
    export let onSend = () => {};
    export let onSaveDraft = () => {};
</script>

<div class="flex items-center gap-10">
    <button class="bg-blaze/80 text-white px-4 py-1.5 rounded hover:bg-blaze transition-all duration-300" on:click={onSend}>
        Send
    </button>
    <button class="bg-white/80 px-4 py-1.5 font-md rounded hover:bg-white hover:font-bold transition-all duration-300" on:click={onSaveDraft}>
        Save Draft
    </button>
</div>
