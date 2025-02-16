<script lang="ts">
    export let activeTab: "send" | "reply";
    export let setActiveTab: (tab: "send" | "reply") => void;
</script>

<div class="flex space-x-4 border-b pb-4">
    <button
            class={`py-2 px-4 rounded border-2 border-stone-300 ${activeTab === 'send' ? 'bg-blaze text-white' : 'bg-mist text-midnight'}`}
            on:click={() => setActiveTab("send")}
    >
        Send Email
    </button>
    <button
            class={`py-2 px-4 rounded border-2 border-stone-300 ${activeTab === 'reply' ? 'bg-blaze text-white' : 'bg-mist text-midnight'}`}
            on:click={() => setActiveTab("reply")}
    >
        Reply Email
    </button>
</div>
