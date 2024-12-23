<script>
    export let onSend = () => {};
    export let onSaveDraft = () => {};
</script>

<div class="flex items-center space-x-2">
    <button
            class="bg-blue-600 text-white px-4 py-1.5 rounded hover:bg-blue-700"
            on:click={onSend}
    >
        Send
    </button>
    <button
            class="bg-gray-200 px-4 py-1.5 rounded hover:bg-gray-300"
            on:click={onSaveDraft}
    >
        Save Draft
    </button>
</div>
